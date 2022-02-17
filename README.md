<p align="center"><a href="https://t.me/SuraVCStreamBot"><img src="https://github.com/SRTheProgrammer/SuraVCStream/raw/main/driver/suravclogo.jpg"></a></p>
<p align="center">
    <br><b>Sura VC Stream is an Advanced Telegram Bot that's allow you to play Video & Music on Telegram Group Video Chat</b><br>
</p>

## Preview
<p align="center">
  <img src="https://telegra.ph/file/21a41d5e4636289c2d768.png">
</p>

## ✨ Features
- Music & Video stream support
- MultiChat support
- Playlist & Queue support
- Skip, Pause, Resume, Stop feature
- Music & Video downloader feature
- Inline Search support
- YouTube direct search support
- YouTube/Local/Live/m3u8 stream support
- Inline Search support
- Control With Button support
- Volume Control
- Userbot Auto Join
- Broadcast & Global Ban
- Shell Executor (eval & sh)
- SpeedTest Runner
- Direct Updater

## 🛠 Commands:
| Command | Description |
| ------ | ------ |
| `/play (query)` | play music from youtube |
| `/vplay (query)` | play video from youtube |
| `/vstream (live link)` | play video live streaming video |
| `/pause` | pause the streaming (admin only) |
| `/resume` | resume the streaming (admin only) |
| `/skip` | switch to next stream (admin only) |
| `/stop` | end the streaming (admin only) |
| `/vmute` | for mute the userbot on voice chat |
| `/vunmute` | for unmute the userbot on voice chat |
| `/volume 1/200` | adjust the volume of userbot (userbot must be admin) |
| `/playlist` | show you all the current stream list |
| `/song (query)` | download music from youtube |
| `/video (query)` | download video from youtube |
| `/userbotjoin` | invite the userbot to join group (admin only) |
| `/userbotleave` | instruct userbot to leave the group (admin only) |
| `/leaveall` | order the userbot to leave from all group (sudo only) |
| `/update` | update your bot directly without leaving telegram (sudo only) |
| `/restart` | restart your bot directly without leaving telegram (sudo only) |
| `/speedtest` | run server speedtest that you use to run your bot |
| `/broadcast` | brodcast message to all group that in bot database |
| `/gban & /ungban` | use this to gban someone and ungban them |
| `/stats` | use this to get stats of your bot |
| `/help` | to show help message in private chat |
| `/ghelp` | to show help message in group chats |



## Generate Pyrogram session string from below

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@SRTheProgrammer/Session-Generator#main.py)

## Heroku Deployment
The easy way to host this bot, deploy to Heroku, Change the app country to Europe (it will help to make the bot stable).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## VPS Deployment 
Get the best Quality of streaming performance by hosting it on VPS, Steps:

```sh
sudo apt update && apt upgrade -y
sudo apt install git curl python3-pip ffmpeg -y
pip3 install -U pip
curl -sL https://deb.nodesource.com/setup_16.x | bash -
sudo apt-get install -y nodejs
npm i -g npm
git clone https://github.com/SRTheProgrammer/SuraVCStream # clone the repo.
cd SuraVCStream
pip3 install -U -r requirements.txt
cp example.env .env # use vim to edit ENVs
vim .env # fill up the ENVs (Steps: press i to enter in insert mode then edit the file. Press Esc to exit the editing mode then type :wq! and press Enter key to save the file).
python3 main.py # run the bot.

# continue the host with screen or anything else, thanks for reading.
```

# Credits 💖
- [Me](https://github.com/SRTheProgrammer) ``Just Modify``
- [Levina](https://github.com/levina-lab) ``Dev``
- [Zxce3](https://github.com/Zxce3) ``Dev``
- [tofikdn](https://github.com/tofikdn) ``Dev``
- [Laky's](https://github.com/Laky-64) for [``py-tgcalls``](https://github.com/pytgcalls/pytgcalls)
- [Dan](https://github.com/delivrance) for [``Pyrogram``](https://github.com/pyrogram)

### Support & Updates 🎑
<a href="https://t.me/SuraBotSupport"><img src="https://img.shields.io/badge/Join-Group%20Support-blue.svg?style=for-the-badge&logo=Telegram"></a> <a href="https://t.me/SuraBotStats"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
