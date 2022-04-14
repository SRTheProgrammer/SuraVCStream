import wget
import speedtest

from PIL import Image
from config import BOT_USERNAME as bname

from driver.filters import command
from driver.decorators import sudo_users_only
from driver.core import bot as app
from driver.utils import remove_if_exists

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(command(["speedtest", f"speedtest@{bname}"]) & ~filters.edited)
@sudo_users_only
async def run_speedtest(_, message: Message):
    m = await message.reply_text("⚡️ running server speedtest")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("⚡️ running download speedtest..")
        test.download()
        m = await m.edit("⚡️ running upload speedtest...")
        test.upload()
        test.results.share()
    except speedtest.ShareResultsConnectFailure:
        pass
    except Exception as e:
        await m.edit(e)
        return
    result = test.results.dict()
    m = await m.edit("🔄 sharing speedtest results")
    if result["share"]:
        path = wget.download(result["share"])
        try:
            img = Image.open(path)
            c = img.crop((17, 11, 727, 389))
            c.save(path)
        except BaseException:
            pass

    output = f"""💡 **SpeedTest Results**
    
<u>**Client:**</u>
**ISP:** {result['client']['isp']}
**Country:** {result['client']['country']}
  
<u>**Server:**</u>
**Name:** {result['server']['name']}
**Country:** {result['server']['country']}, {result['server']['cc']}
**Sponsor:** {result['server']['sponsor']}
**Latency:** {result['server']['latency']}
⚡️ **Ping:** {result['ping']}"""
    if result["share"]:
        msg = await app.send_photo(
            chat_id=message.chat.id, photo=path, caption=output
        )
        remove_if_exists(path)
    else:
        msg = await app.send_message(
            chat_id=message.chat.id, text=output
        )
    await m.delete()
