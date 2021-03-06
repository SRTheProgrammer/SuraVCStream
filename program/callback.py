# Copyright (C) 2022 By SuraVCProject

from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_USERNAME,
    BG_IMG,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""π **Welcome {query.message.from_user.mention()} !**\n
π€ [{me_bot.first_name}](https://t.me/{me_bot.username}) **Allows you to play musicπΆ and videoπ₯ on groups through the Telegram Group video chat!**\n
π **Find out all the Bot's commands and how they work by clicking on the Β» π οΈ Check Commands button!**\n
π **To know how to use this bot, please click on the Β» π Read Basic Guide button!**\n
π½ **To Deploy Your Own Source Click On The Β» π My Source Code Button **\n """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Add me to your Group β",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("π Basic Guide", callback_data="user_guide")],
                [
                    InlineKeyboardButton("π οΈ Commands", callback_data="command_list"),
                    InlineKeyboardButton("π² Donate", url=f"https://t.me/{OWNER_USERNAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "π¨πΎβπ€βπ¨πΌ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "π Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "π My Source Code", url="https://github.com/SRTheProgrammer/SuraVCStream"
                    )
                ],
                [    InlineKeyboardButton(
                    "βοΈβ οΈYoutube Channelβ οΈβοΈ", url="https://www.youtube.com/channel/UCCmjxoJe_6T1ota84YH3ikg?sub_confirmation=1"
                     )
                ],
                [
                    InlineKeyboardButton(
                    "Mining βΏitcoin", url="http://t.me/ProBTCMinerbot?start=ref1261923198"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
        
@Client.on_callback_query(filters.regex("help_command"))
@check_blacklist()
async def help(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("help message")
    await query.edit_message_text(
        f""" β¨ **Hello [{query.message.chat.first_name}] !**\n
π· **To Know How to setup this Bot? Read π€ Setting Up This Bot in Group **\n
π· **To Know Play Video/Audio/Live? Read βοΈ Quick Use Commands **\n
π· **To Know Every Single Command Of Bot? Read π All Commands**\n """,
        reply_markup=InlineKeyboardMarkup(
        
        [
            [
                InlineKeyboardButton(
                    "π€ Setting Up This Bot in Group", callback_data="user_guide"
                )
            ],
            [
                InlineKeyboardButton(
                    "βοΈ Quick Use Commands", callback_data="quick_use"
                )
            ],
            [
                InlineKeyboardButton(
                    "π All Commands", callback_data="command_list"
                )
            ],
            [
                InlineKeyboardButton(
                    "π Go Back", callback_data="home_start"
                )
            ],
            [
                InlineKeyboardButton("π¨πΎβπ€βπ¨πΌ Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "π Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
            
        ]      
  ),
    disable_web_page_preview=True,
    )
 

@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""βΉοΈ Quick use Guide bot, please read fully !

Β» /play - Type this with give the song title or youtube link or audio file to play Music. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

Β» /vplay - Type this with give the song title or youtube link or video file to play Video. (Remember to don't play YouTube live video by using this command!, because it will cause unforeseen problems.)

Β» /vstream - Type this with give the YouTube live stream video link or m3u8 link to play live Video. (Remember to don't play local audio/video files or non-live YouTube video by using this command!, because it will cause unforeseen problems.)

β Still Have questions? Contact us in [Support Group](https://t.me/{GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("π Go Back to Bot Setup", callback_data="user_guide")],
                [InlineKeyboardButton("π Go Back to Help", callback_data="help_command")]    
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""β How to Setup This Bot in Group ?, read the Guide below !

1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{me_user.username} to your group or type /userbotjoin to invite her, unfortunately the userbot will joined by itself when you use song playing commands.
4.) Turn on/Start the video chat first before start to play video/music.

Read 
`- END, EVERYTHING HAS BEEN SETUP -`

π If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.

π‘ If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Β» Quick use Guide Β«", callback_data="quick_use")
                ],[
                    InlineKeyboardButton("π Go Back to Start", callback_data="home_start")
                ],[
                    InlineKeyboardButton("π Go Back to Help", callback_data="help_command")
                ]
            ]   
      ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""β¨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

Β» Check out the menu below to read the module information & see the list of available Commands !

All commands can be used with (`! / .`) handler""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π?π»ββοΈ Admins Commands", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("π©π»βπΌ Users Commands", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("Sudo Commands", callback_data="sudo_command"),
                    InlineKeyboardButton("Owner Commands", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("π Go Back to Start", callback_data="home_start")
                ],[
                    InlineKeyboardButton("π Go Back to Help", callback_data="help_command")
                ]
                   
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""βοΈ Command list for all user.
        
Β» /play (song name/youtube link) - play the music from youtube
Β» /stream (m3u8/youtube live link) - play youtube/m3u8 live stream music
Β» /vplay (video name/youtube link) - play the video from youtube
Β» /vstream (m3u8/youtube live link) - play youtube/m3u8 live stream video
Β» /playlist - view the queue list of songs and current playing song
Β» /lyric (query) - search for song lyrics based on the name of the song
Β» /video (query) - download video from youtube
Β» /song (query) - download song from youtube
Β» /search (query) - search for the youtube video link
Β» /ping - show the bot ping status
Β» /uptime - show the bot uptime status
Β» /alive - show the bot alive info (in Group only)
Β» /help - to Show Help Message (Full Bot Guide)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""βοΈ Command list for group admin.

Β» /pause - pause the current track being played
Β» /resume - play the previously paused track
Β» /skip - goes to the next track
Β» /stop - stop playback of the track and clears the queue
Β» /vmute - mute the streamer userbot on group call
Β» /vunmute - unmute the streamer userbot on group call
Β» /volume `1-200` - adjust the volume of music (userbot must be admin)
Β» /reload - reload bot and refresh the admin data
Β» /userbotjoin - invite the userbot to join group
Β» /userbotleave - order userbot to leave from group
Β» /startvc - start/restart the group call
Β» /stopvc - stop/discard the group call""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    if user_id not in SUDO_USERS:
        await query.answer("β οΈ You don't have permissions to click this button\n\nΒ» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""βοΈ Command list for sudo user.

Β» /stats - get the bot current statistic
Β» /calls - show you the list of all active group call in database
Β» /block (`chat_id`) - use this to blacklist any group from using your bot
Β» /unblock (`chat_id`) - use this to whitelist any group from using your bot
Β» /blocklist - show you the list of all blacklisted chat
Β» /speedtest - run the bot server speedtest
Β» /sysinfo - show the system informatio
Β» /logs - generate the current bot logs
Β» /eval - run an code
Β» /sh - run an code""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    if user_id not in OWNER_ID:
        await query.answer("β οΈ You don't have permissions to click this button\n\nΒ» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""βοΈ Command list for bot owner.

Β» /gban (`username` or `user_id`) - for global banned people, can be used only in group
Β» /ungban (`username` or `user_id`) - for un-global banned people, can be used only in group
Β» /update - update your bot to latest version
Β» /restart - restart your bot server
Β» /leaveall - order userbot to leave from all group
Β» /leavebot (`chat id`) - order bot to leave from the group you specify
Β» /broadcast (`message`) - send a broadcast message to all groups in bot database
Β» /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin""",

        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("β Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("β nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("β Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("β Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
