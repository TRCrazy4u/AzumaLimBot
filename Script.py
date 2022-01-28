class script(object):
    START_TXT = """Hᴇʟʟᴏ {},
Mʏ Nᴀᴍᴇ ɪs <b>Aᴢᴜᴍᴀ Lɪᴍ</b>, A Sᴍᴀʀᴛ Rᴏʙᴏᴛ ᴡɪᴛʜ Mᴀɴʏ Aᴍᴀᴢɪɴɢ ғᴇᴀᴛᴜʀᴇs ᴀʟsᴏ I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs, Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs & Eɴᴊᴏʏ!"""
    HELP_TXT = """ʜᴇʏ {}
Hᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴜ:"""
    ABOUT_TXT = """➲ Mʏ ɴᴀᴍᴇ: Aᴢᴜᴍᴀ Lɪᴍ
➲ Cʀᴇᴀᴛᴏʀ: <a href=https://t.me/TRCrazy>Ʈᖇ ᙅɾᥲⱬყ</a>
➲ Lɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org/>Pʏʀᴏɢʀᴀᴍ</a>
➲ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org/>Pʏᴛʜᴏɴ 3</a>
➲ Dᴀᴛᴀʙᴀsᴇ: <a href=https://cloud.mongodb.com/>Mᴏɴɢᴏ DB</a>
➲ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href=https://heroku.com/>Hᴇʀᴏᴋᴜ</a>
➲ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v1.0.1 [ Bᴇᴛᴀ ]"""
    SOURCE_TXT = """<b>Nᴏᴛᴇ:</b>
Dᴇᴠ:
• <a href=https://t.me/TRCrazy>Ʈᖇ ᙅɾᥲⱬყ</a>
Nᴏᴛᴇ:
• Aᴢᴜᴍᴀ ɪs ᴀ ᴄʟᴏsᴇ sᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.
• Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠs ᴏɴʟʏ ғᴏʀ ʀᴇᴘᴏʀᴛɪɴɢ ʙᴜɢs."""
    MANUELFILTER_TXT = """Hᴇʟᴘ: <b>Fɪʟᴛᴇʀs</b>
- ғɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ᴇᴠᴀᴍᴀʀɪᴀ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ
<b>Nᴏᴛᴇ:</b>
1. Aᴢᴜᴍᴀ Lɪᴍ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 𝟼𝟺 ᴄʜᴀʀᴀᴄᴛᴇʀs.
<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• /filter - <code>ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""
    
    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴs</b>

- ᴀᴢᴜᴍᴀ sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>ɴᴏᴛᴇ:</b>
𝟷. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
𝟸. ᴀᴢᴜᴍᴀ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
𝟹. ʙᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonurl:https://t.me/AzumaLimBot)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ғɪʟᴛᴇʀ</b>

<b>ɴᴏᴛᴇ:</b>
𝟷. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
𝟸. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇs.
𝟹. ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇs.
 ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""
    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴs</b>

- ᴜsᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs.

<b>ɴᴏᴛᴇ:</b>
𝟷. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
𝟸. sᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ ᴘᴍ

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Azuma

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ᴛᴏᴛᴀʟ ғɪʟᴇs: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>
★ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱
★ ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
ɢʀᴏᴜᴘ = {}(<code>{}</code>)
ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs = <code>{}</code>
ᴀᴅᴅᴇᴅ ʙʏ - {}
"""
    LOG_TEXT_P = """#NewUser
ɪᴅ - <code>{}</code>
ɴᴀᴍᴇ - {}
"""
