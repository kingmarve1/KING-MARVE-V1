from telethon import TelegramClient, events, functions, types
import asyncio
from telethon.tl.functions.messages import SetTypingRequest
from telethon.tl.types import SendMessageTypingAction
from deep_translator import GoogleTranslator
from datetime import datetime, timedelta
from PIL import Image
import os
from collections import defaultdict
from telethon.tl.custom import Message
from gtts import gTTS
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.types import ChannelParticipantsSearch
import time  # Put this at the top with other imports
import random
from telethon.tl.functions.contacts import SearchRequest
import aiohttp
import json
from telethon import events, Button

# Store the start time of the bot
start_time = time.time()
auto_reply_enabled = False  # default OFF

 #🔄 Global flag
auto_react_enabled = False

# Replace this with your actual Telegram user ID
OWNER_ID = 8076230542

# Store messages per chat_id
message_cache = defaultdict(dict)
antidelete_on_groups = set()
antidelete_on_groups = set()

# 🟨 Step 1: Replace these with your real values
api_id = 24081964
api_hash = 'b2f302aefe5684c3fa932b9648e94d5b'

# 🟩 Step 2: Create the session file
client = TelegramClient('userbot', api_id, api_hash)

# 🟦 Step 3: Bot Commands
welcome_enabled = {}

@client.on(events.NewMessage(pattern=r'.menu'))
async def menu_handler(event):
    image_url = "https://files.catbox.moe/cqitqv.png"

    caption = """
``` 🌑 𝗥𝗘𝗔𝗣𝗘𝗥 𝗫 𝗠𝗗  
👑 𝗖𝗿𝗲𝗮𝘁𝗼𝗿: Lord Nagato x Drenox
🔥 𝗛𝗼𝘀𝘁𝗲𝗱 𝗼𝗻: LINUX  
📞 𝗖𝗢𝗡𝗧𝗔𝗖𝗧: [t.me/Officialnagatoblaq_1]
(https://t.me/the_incernate)

╔═────────────══╗  
 ⚙️ 𝗕𝗢𝗧𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 ⚙️  
╚═────────────══╝  

🟢 .ping  
ℹ️ .about  
👋 .hello  
👁️ .vv  
🖼️ .sticker  
🏷️ .tagall  
🔨 .ban  
♻️ .unban  
👢 .kick  
🔇 .mute  
🔊 .unmute  
🆙 .promote  
⬇️ .demote  
📌 .pin  
📍 .unpin  
🗑️ .delete  
🔒 .lock  
🔓 .unlock  
🥶 .antilink on  
🥱 .antilink off  
🛡️ .antidelete on  
🛡️ .antidelete off  
🚫 .block  
😁 .unblock
🛑 .private on  
✅ .private off  
🔗 .linkgc  
💬 .setwelcome  
📍 .track
😇 .tovnote
🤑 .purchase
🤐 .info
😁 .pickuplines
💀 .bug
🤡 .uptime
🐍 .snake @username
🤯 .autoreply on
👽 .autoreply off
🤯 .toimage
😬 .gpt
😵 .get
🤕 .pp
👀 .toimage
🤫 .autoreact
👿 .clearadmins
😌 .channel
🤑 .owner


╔═────────────╗  
   🔔 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗢𝗻𝗹𝗶𝗻𝗲  
╚═────────────╝  

💀 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆: *** LORD NAGATO X DRENOX**  ```
"""
    await client.send_file(event.chat_id, image_url, caption=caption)

@client.on(events.NewMessage(pattern=r"\.ping"))
async def stylish_ping(event):
    start = time.time()
    ping_msg = await event.reply("🌑")
    await ping_msg.edit("🌑.x.")  # REAPER Vibe
    await ping_msg.edit("🌑..x..")
    await ping_msg.edit("🌑...x...")
    await ping_msg.edit("♻️ Calculating speed...")
    
    end = time.time()
    ping_time = int((end - start) * 1000)

    await ping_msg.edit(f"""
╔═━━━━✪『𝐑𝐄𝐀𝐏𝐄𝐑 𝐗 𝐌𝐃』✪━━━━═╗

🏓 𝗣𝗼𝗻𝗴 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲!
⚡ 𝗦𝗽𝗲𝗲𝗱: `{ping_time}ms`
🧠 𝗦𝘁𝗮𝘁𝘂𝘀: `Online`

╚═══════✪✪═══════╝
""")

@client.on(events.NewMessage(pattern=r"\.channel"))
async def channel_handler(event):
    await event.respond(
        "**📡 Official Channel for Updates!**\n\nJoin to get scripts, support & REAPER X MD tools.",
        buttons=[
            [Button.url("🔗 Join TAILUNG TECH", "https://t.me/thetailungtech")]
        ]
    )

@client.on(events.NewMessage(pattern=r"\.purchase"))
async def purchase_handler(event):
    msg = """💸 *Reaper X Script Pricing* 💸

📄 Without Encryption: `$7`
🛡️ With Encryption: `$3`
🔓 Non-Encrypted Source Code: `$4`
🔐 Encrypted Source Code: `$6`

💬 To buy, message: [@Officialnagatoblaq_1]
(@the_incernate)
"""
    await event.reply(msg, link_preview=False, parse_mode='md')
    
@client.on(events.NewMessage(pattern=r'.about'))
async def about_handler(event):
    await event.reply("I'm a simple UserBot made by lord nagato with the assistance of drenox use well and enjoy")

@client.on(events.NewMessage(pattern=r'.hello'))
async def hello_handler(event):
    await event.reply("👋 Hello from your UserBot!")

@client.on(events.NewMessage(pattern=r'.kick'))
async def kick_handler(event):
    if not event.is_group:
        await event.reply("❌ This command can only be used in a group.")
        return

    if not event.is_reply:
        await event.reply("⚠️ Please reply to the user's message you want to kick.")
        return

    try:
        reply = await event.get_reply_message()
        user = await client.get_entity(reply.sender_id)

        await client.kick_participant(event.chat_id, user.id)
        await client.edit_permissions(event.chat_id, user.id, view_messages=True)
        await event.reply(f"👢 Kicked [{user.first_name}](tg://user?id={user.id})")

    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")

@client.on(events.NewMessage(pattern=r"\.promote"))
async def promote_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    if not event.is_reply:
        await event.reply("⚠️ Please reply to the user's message you want to promote.")
        return

    try:
        reply = await event.get_reply_message()
        user = await client.get_entity(reply.sender_id)

        rights = ChatAdminRights(
            post_messages=True,
            add_admins=False,
            invite_users=True,
            change_info=False,
            ban_users=True,
            delete_messages=True,
            pin_messages=True,
            manage_call=True,
            anonymous=False,
            manage_chat=True
        )

        await client.edit_admin(
            entity=event.chat_id,
            user=user.id,
            rights=rights,
            rank="Admin"  # You can change the title if you want
        )

        await event.reply(f"✅ Promoted [{user.first_name}](tg://user?id={user.id}) to Admin!")

    except Exception as e:
        await event.reply(f"❌ Failed to promote: `{e}`")


@client.on(events.NewMessage(pattern=r"\.bug (.+)"))
async def hi_spam_by_name(event):
    name = event.pattern_match.group(1).strip()
    try:
        result = await client(SearchRequest(
            q=name,
            limit=1
        ))
        if not result.users:
            await event.reply("❌ User not found.")
            return
        user = result.users[0]
        for _ in range(45):
            await client.send_message(user, "🌟ཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱཱིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀིྀꦾ")
        await event.reply(f"✅ Successfullysent bugs Powered By drenox X Nagato")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")
        

@client.on(events.NewMessage(pattern=r"\.demote"))
async def demote_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    if not event.is_reply:
        await event.reply("⚠️ Please reply to the user's message you want to demote.")
        return

    try:
        reply = await event.get_reply_message()
        user = await client.get_entity(reply.sender_id)

        no_rights = ChatAdminRights(
            post_messages=False,
            add_admins=False,
            invite_users=False,
            change_info=False,
            ban_users=False,
            delete_messages=False,
            pin_messages=False,
            manage_call=False,
            anonymous=False,
            manage_chat=False
        )

        await client.edit_admin(
            entity=event.chat_id,
            user=user.id,
            rights=no_rights,
            rank=""
        )

        await event.reply(f"🧨 Demoted [{user.first_name}](tg://user?id={user.id}) successfully!")

    except Exception as e:
        await event.reply(f"❌ Error while demoting: `{e}`")
        
@client.on(events.NewMessage(pattern=r"\.clearadmins"))
async def clear_admins(event):
    if not event.is_group:
        await event.reply("❌ This command only works in groups.")
        return

    me = await client.get_me()
    my_id = me.id
    chat = await event.get_chat()

    await event.reply("🔍 Scanning admins...")

    try:
        async for user in client.iter_participants(chat.id, filter=ChannelParticipantsAdmins):
            if user.id != my_id and not user.bot:
                try:
                    no_rights = ChatAdminRights(
                        post_messages=False,
                        add_admins=False,
                        invite_users=False,
                        change_info=False,
                        ban_users=False,
                        delete_messages=False,
                        pin_messages=False,
                        manage_call=False,
                        anonymous=False,
                        manage_chat=False
                    )

                    await client(EditAdminRequest(
                        channel=chat,
                        user_id=user.id,
                        rights=no_rights,
                        rank=""
                    ))

                    await event.reply(f"🧨 Demoted: [{user.first_name}](tg://user?id={user.id})")

                except Exception as e:
                    await event.reply(f"❌ Failed to demote {user.first_name}: {e}")

        await event.reply("✅ Done! All admins (except you) have been demoted.")

    except Exception as e:
        await event.reply(f"❌ Error: {e}")

@client.on(events.NewMessage(pattern=r'.mute(?: (\d+))?'))
async def mute_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    if not event.is_reply:
        await event.reply("⚠️ Please reply to the user's message you want to mute.")
        return

    try:
        reply = await event.get_reply_message()
        user = await client.get_entity(reply.sender_id)

        args = event.pattern_match.group(1)
        duration_minutes = int(args) if args else None

        if duration_minutes:
            until_date = datetime.utcnow() + timedelta(minutes=duration_minutes)
        else:
            until_date = None

        rights = ChatBannedRights(
            until_date=until_date,
            send_messages=True
        )

        await client.edit_permissions(event.chat_id, user.id, rights)

        if duration_minutes:
            await event.reply(f"🔇 Muted [{user.first_name}](tg://user?id={user.id}) for {duration_minutes} minutes.")
        else:
            await event.reply(f"🔇 Muted [{user.first_name}](tg://user?id={user.id}) permanently.")

    except Exception as e:
        await event.reply(f"❌ Error while muting: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.unmute'))
async def unmute_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    if not event.is_reply:
        await event.reply("⚠️ Please reply to the muted user's message to unmute them.")
        return

    try:
        reply = await event.get_reply_message()
        user = await client.get_entity(reply.sender_id)

        rights = ChatBannedRights(
            until_date=None,
            send_messages=False  # False means allow messages again
        )

        await client.edit_permissions(event.chat_id, user.id, rights)

        await event.reply(f"🔊 Unmuted [{user.first_name}](tg://user?id={user.id}) successfully!")

    except Exception as e:
        await event.reply(f"❌ Error while unmuting: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.ban'))
async def ban_handler(event):
    if not event.is_group:
        await event.reply("❌ This command can only be used in group chats.")
        return

    if not event.is_reply:
        await event.reply("⚠️ Please reply to the user's message you want to ban.")
        return

    try:
        reply = await event.get_reply_message()
        user = await client.get_entity(reply.sender_id)

        rights = ChatBannedRights(
            until_date=None,
            view_messages=True  # True = ban from seeing messages
        )

        await client.edit_permissions(event.chat_id, user.id, rights)

        await event.reply(f"🔨 Banned [{user.first_name}](tg://user?id={user.id}) from the group!")

    except Exception as e:
        await event.reply(f"❌ Error while banning: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.unban'))
async def unban_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    if not event.is_reply:
        await event.reply("⚠️ Please reply to the banned user's message to unban them.")
        return

    try:
        reply = await event.get_reply_message()
        user = await client.get_entity(reply.sender_id)

        rights = ChatBannedRights(
            until_date=None,
            view_messages=False  # False = allow to see messages again (unban)
        )

        await client.edit_permissions(event.chat_id, user.id, rights)

        await event.reply(f"✅ Unbanned [{user.first_name}](tg://user?id={user.id}) successfully!")

    except Exception as e:
        await event.reply(f"❌ Error while unbanning: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.info'))
async def info_handler(event):
    if not event.is_reply:
        await event.reply("⚠️ Please reply to a user's message to get their info.")
        return

    try:
        reply = await event.get_reply_message()
        user = await client.get_entity(reply.sender_id)

        info = f"""
👤 **User Info**

🆔 ID: `{user.id}`
📛 Name: {user.first_name or ""} {user.last_name or ""}
🔗 Username: @{user.username if user.username else "N/A"}
🌐 Bot: {"Yes" if user.bot else "No"}
⛓️ Scammer: {"Yes" if getattr(user, "scam", False) else "No"}
📅 Account Created: {user.date if hasattr(user, "date") else "N/A"}
        """

        await event.reply(info)

    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.lock'))
async def lock_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    try:
        rights = ChatBannedRights(
            send_messages=True
        )

        await client.edit_permissions(event.chat_id, rights=rights)
        await event.reply("🔒 Group has been locked. Only admins can send messages now.")

    except Exception as e:
        await event.reply(f"❌ Error while locking: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.unlock'))
async def unlock_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    try:
        rights = ChatBannedRights(
            send_messages=False
        )

        await client.edit_permissions(event.chat_id, rights=rights)
        await event.reply("🔓 Group has been unlocked. Everyone can chat now.")

    except Exception as e:
        await event.reply(f"❌ Error while unlocking: {str(e)}")
      
@client.on(events.NewMessage)
async def cache_messages(event):
    if event.is_group and event.chat_id in antidelete_on_groups:
        message_cache[event.chat_id][event.id] = event
        
@client.on(events.MessageDeleted())
async def on_message_deleted(event):
    if event.chat_id not in antidelete_on_groups:
        return

    for msg_id in event.deleted_ids:
        deleted_msg = message_cache[event.chat_id].get(msg_id)
        if deleted_msg:
            sender = await deleted_msg.get_sender()
            sender_name = f"[{sender.first_name}](tg://user?id={sender.id})"
            content = deleted_msg.text or "<media>"
            
            await client.send_message(
                event.chat_id,
                f"🚨 Message deleted by {sender_name}:\n\n{content}"
            )
        
@client.on(events.NewMessage(pattern=r'\.pin'))
async def pin_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    if not event.is_reply:
        await event.reply("⚠️ Please reply to the message you want to pin.")
        return

    try:
        reply = await event.get_reply_message()
        await client.pin_message(event.chat_id, message=reply.id, notify=False)
        await event.reply("📌 Message pinned successfully!")

    except Exception as e:
        await event.reply(f"❌ Error while pinning: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.unpin'))
async def unpin_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    try:
        # Unpin the last pinned message
        await client.unpin_message(event.chat_id)
        await event.reply("📍 Last pinned message has been unpinned!")

    except Exception as e:
        await event.reply(f"❌ Error while unpinning: {str(e)}")
        
antilink_enabled = {}

@client.on(events.NewMessage(pattern=r'\.antilink (on|off)'))
async def antilink_toggle(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    action = event.pattern_match.group(1)
    chat_id = event.chat_id

    if action == "on":
        antilink_enabled[chat_id] = True
        await event.reply("🔒 Antilink has been **enabled**. Group invite links will now be deleted.")
    else:
        antilink_enabled[chat_id] = False
        await event.reply("🔓 Antilink has been **disabled**. Users can now send invite links.")

@client.on(events.NewMessage)
async def antilink_checker(event):
    chat_id = event.chat_id

    # Skip if not a group or antilink is off
    if not event.is_group or not antilink_enabled.get(chat_id, False):
        return

    if "t.me/joinchat" in event.raw_text or "t.me/" in event.raw_text or "telegram.me/" in event.raw_text:
        try:
            await event.delete()
            await client.send_message(chat_id, f"🚫 Link deleted: [{event.sender.first_name}](tg://user?id={event.sender_id})", parse_mode='md')
        except Exception as e:
            print(f"Failed to delete message: {e}")
            
@client.on(events.NewMessage(pattern=r'\.antilink off'))
async def antilink_off_handler(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    chat_id = event.chat_id
    antilink_enabled[chat_id] = False
    await event.reply("🔓 Antilink has been **disabled**. Users can now send links.")

@client.on(events.NewMessage(pattern=r'\.sticker'))
async def image_to_sticker(event):
    if not event.is_reply:
        await event.reply("⚠️ Please reply to an image to convert to sticker.")
        return

    reply = await event.get_reply_message()

    if not reply.media:
        await event.reply("❌ That message doesn't contain an image.")
        return

    try:
        # Step 1: Download the image
        img_path = await reply.download_media()
        sticker_path = "sticker.webp"

        # Step 2: Open, resize, and convert to webp using Pillow
        with Image.open(img_path) as im:
            im = im.convert("RGBA")
            im.thumbnail((512, 512))
            im.save(sticker_path, "WEBP")

        # Step 3: Send as sticker from the bot
        await client.send_file(
            event.chat_id,
            sticker_path,
            force_document=False,
            allow_cache=False,
            reply_to=event.reply_to_msg_id
        )

        await event.reply("✅ Sticker created!")

        # Step 4: Clean up
        os.remove(img_path)
        os.remove(sticker_path)

    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")

autotyping_enabled = False
autotyping_task = None

@client.on(events.NewMessage(pattern=r"\.autotyping (on|off)"))
async def toggle_autotyping(event):
    global autotyping_enabled, autotyping_task

    action = event.pattern_match.group(1)

    if action == "on":
        if autotyping_enabled:
            await event.reply("✏️ AutoTyping is already running.")
            return

        autotyping_enabled = True
        await event.reply("✏️ AutoTyping **Enabled**.\nNow showing typing... in all groups.")

        async def run_typing_loop():
            while autotyping_enabled:
                async for dialog in client.iter_dialogs():
                    if dialog.is_group or dialog.is_channel:
                        try:
                            await client(SetTypingRequest(
                                peer=dialog.id,
                                action=SendMessageTypingAction()
                            ))
                        except Exception:
                            pass
                await asyncio.sleep(5)  # Type every 5 seconds

        autotyping_task = asyncio.create_task(run_typing_loop())

    elif action == "off":
        autotyping_enabled = False
        if autotyping_task:
            autotyping_task.cancel()
        await event.reply("❌ AutoTyping **Disabled**.")
       
@client.on(events.NewMessage(pattern=r'\.vv'))
async def reveal_view_once_handler(event):
    if not event.is_reply:
        await event.reply("⚠️ Reply to a view-once image or video to reveal it.")
        return

    try:
        reply = await event.get_reply_message()

        if not reply.media:
            await event.reply("❌ That message doesn't contain any media.")
            return

        # Download view-once media before it's viewed
        file_path = await reply.download_media()

        # Re-send it as normal
        await client.send_file(event.chat_id, file_path, caption="🔓 View Once Media Unlocked!")

        await event.reply("✅ Done! The media has been revealed.")

        # Optional: delete the file after sending
        import os
        os.remove(file_path)

    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")
        
        


@client.on(events.NewMessage(pattern=r"\.gpt (.+)"))
async def gpt_command(event):
    import aiohttp
    import json

    prompt = event.pattern_match.group(1)
    thinking = await event.reply("🤖 Thinking...")

    try:
        url = "https://api.together.xyz/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 8d120426695a7c38c7c7b8f28fc0a199b5c5db2f557d7c32392a7e83c110d3fa"
        }
        payload = {
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    reply = result["choices"][0]["message"]["content"]
                    await thinking.edit(f"💡 {reply}")
                else:
                    error_text = await resp.text()
                    await thinking.edit(f"⚠️ API error {resp.status}:\n{error_text}")

    except Exception as e:
        await thinking.edit(f"❌ Error: {e}")
        
@client.on(events.NewMessage(pattern=r'\.delete'))
async def delete_handler(event):
    if not event.is_reply:
        await event.reply("⚠️ Please reply to the message you want to delete.")
        return

    try:
        reply = await event.get_reply_message()
        deleted_text = reply.message or "<media>"
        
        await client.delete_messages(event.chat_id, reply.id)

        await event.reply(f"🗑️ Deleted message:\n\n`{deleted_text}`")
    except Exception as e:
        await event.reply(f"❌ Error while deleting: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.antidelete (on|off)'))
async def antidelete_toggle(event):
    if not event.is_group:
        await event.reply("❌ This command only works in group chats.")
        return

    cmd = event.pattern_match.group(1)

    if cmd == "on":
        antidelete_on_groups.add(event.chat_id)
        await event.reply("🛡️ Anti-Delete has been **enabled** for this group.")
    else:
        antidelete_on_groups.discard(event.chat_id)
        await event.reply("🚫 Anti-Delete has been **disabled** for this group.")
        
@client.on(events.MessageDeleted())
async def on_message_deleted(event):
    if event.chat_id not in antidelete_on_groups:
        return

    for msg_id in event.deleted_ids:
        try:
            deleted_msg = await client.get_messages(event.chat_id, ids=msg_id)

            if deleted_msg:
                sender = await deleted_msg.get_sender()
                sender_name = f"[{sender.first_name}](tg://user?id={sender.id})"
                text = deleted_msg.text or "<media>"

                await client.send_message(
                    event.chat_id,
                    f"🚨 **Deleted message by {sender_name}:**\n\n{text}"
                )
        except Exception as e:
            print(f"Error handling deleted message: {e}")
            
autotyping_enabled = {}
@client.on(events.ChatAction)
async def welcome_user(event):
    chat_id = event.chat_id
    if not welcome_enabled.get(chat_id, False):
        return

    if event.user_joined or event.user_added:
        user = await event.get_user()
        chat = await event.get_chat()
        name = user.first_name or "friend"
        title = chat.title or "this group"

        welcome_message = f"""╭━━━〔 👋 𝐍𝐄𝐖 𝐌𝐄𝐌𝐁𝐄𝐑 𝐀𝐋𝐄𝐑𝐓 〕━━━╮

👤 𝗡𝗮𝗺𝗲: {name}
🏠 𝗚𝗿𝗼𝘂𝗽: {title}

🪄 You're now part of something cool 😎  
✨ 𝗘𝗻𝗷𝗼𝘆 𝘁𝗵𝗲 𝘃𝗶𝗯𝗲𝘀 & 𝘀𝘁𝗮𝘆 𝗮𝘄𝗲𝘀𝗼𝗺𝗲!

╰━━━━━━━━━━━━━━━━━━━━━━━╯"""

        await event.reply(welcome_message)
        
@client.on(events.NewMessage(pattern=r"\.setwelcome (on|off)$"))
async def toggle_welcome(event):
    if not event.is_group:
        return await event.reply("❌ This command only works in groups.")

    # Check if sender is admin
    try:
        user = await event.get_sender()
        chat = await event.get_chat()
        participant = await client(functions.channels.GetParticipantRequest(
            channel=chat,
            participant=user.id
        ))
        if not isinstance(participant.participant, (types.ChannelParticipantAdmin, types.ChannelParticipantCreator)):
            return await event.reply("🚫 Only admins can use this command.")
    except:
        return await event.reply("⚠️ Couldn't verify admin rights.")

    # Set welcome state
    status = event.pattern_match.group(1).lower()
    chat_id = event.chat_id

    if status == "on":
        welcome_enabled[chat_id] = True
        await event.reply("✅ Welcome is now **enabled** in this group.")
    else:
        welcome_enabled[chat_id] = False
        await event.reply("🚫 Welcome is now **disabled** in this group.")
        

@client.on(events.NewMessage(pattern=r"\.autotyping (on|off)"))
async def autotyping_toggle(event):
    chat_id = event.chat_id
    action = event.pattern_match.group(1).lower()

    if action == "on":
        autotyping_enabled[chat_id] = True
        await event.reply("🟢 AutoTyping is now ON in this chat.")

        while autotyping_enabled.get(chat_id, False):
            try:
                await client(functions.messages.SetTypingRequest(
                    peer=chat_id,
                    action=types.SendMessageTypingAction()
                ))
                await asyncio.sleep(5)
            except Exception as e:
                await event.reply(f"❌ Typing Error: {str(e)}")
                break

    else:
        autotyping_enabled[chat_id] = False
        await event.reply("🔴 AutoTyping is now OFF in this chat.")
        
@client.on(events.NewMessage(pattern=r"\.tovnote"))
async def to_vnote_handler(event):
    if not event.is_reply:
        await event.reply("⚠️ Please reply to a text message to convert it to a voice note.")
        return

    reply = await event.get_reply_message()

    if not reply.text:
        await event.reply("❌ That message doesn't contain any text.")
        return

    try:
        tts = gTTS(reply.text, lang="en")
        tts.save("voice.ogg")

        # Send as voice note
        await client.send_file(
            event.chat_id,
            "voice.ogg",
            voice_note=True,
            reply_to=reply.id
        )

        os.remove("voice.ogg")
        await event.delete()

    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")
        


@client.on(events.NewMessage(pattern=r'\.private(?: (on|off))?'))
async def private_mode(event):
    if event.sender_id != OWNER_ID:
        await event.reply("🚫 You are not allowed to use this command.")
        return

    mode = event.pattern_match.group(1)
    if not mode:
        await event.reply("ℹ️ Usage: `.private on` or `.private off`")
        return

    if mode == "on":
        global PRIVATE_MODE
        PRIVATE_MODE = True
        await event.reply("🔐 Private mode is now ON. Only you can use commands.")
    else:
        PRIVATE_MODE = False
        await event.reply("🔓 Private mode is now OFF. Everyone can use commands.")
      
@client.on(events.NewMessage(pattern=r'\.track'))
async def fake_track(event):
    reply = await event.get_reply_message()
    if not reply:
        await event.reply("❗Please reply to a user's message to track.")
        return

    await event.reply(f"🛰️ Tracking user `{reply.sender_id}`...\n✅ Approximate location found: Lagos, Nigeria\n🌐 https://maps.google.com/?q=6.5244,3.3792")
    
@client.on(events.NewMessage(pattern=r"\.unblock(?:\s+@?(\w+))?"))
async def unblock_user(event):
    try:
        # Check if username or reply was used
        username = event.pattern_match.group(1)

        if username:
            user = await client.get_entity(username)
        elif event.is_reply:
            reply_msg = await event.get_reply_message()
            user = await client.get_entity(reply_msg.sender_id)
        else:
            await event.reply("⚠️ Please reply to a user or give their @username.")
            return

        await client(functions.contacts.UnblockRequest(id=user.id))
        await event.reply(f"✅ Successfully unblocked [{user.first_name}](tg://user?id={user.id})", parse_mode="md")

    except Exception as e:
        await event.reply(f"❌ Error while unblocking: `{str(e)}`")

@client.on(events.NewMessage(pattern=r'\.block'))
async def block_user(event):
    # Only allow the owner to use it
    if event.sender_id != YOUR_USER_ID:  # ← Replace with your Telegram user ID
        return

    if event.is_private:
        await event.client(functions.contacts.BlockRequest(event.chat_id))
        await event.reply("✅ User has been blocked.")
    elif event.reply_to_msg_id:
        reply = await event.get_reply_message()
        await event.client(functions.contacts.BlockRequest(reply.sender_id))
        await event.reply("✅ Replied user has been blocked.")
    else:
        await event.reply("❌ Error: Please reply to a user to block them.")
        

@client.on(events.NewMessage(pattern=r"\.translate(?: (\w+))?"))
async def reply_translate(event):
    lang = event.pattern_match.group(1)

    if not lang:
        languages = """
🌐 **𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘𝗦 𝗬𝗢𝗨 𝗖𝗔𝗡 𝗨𝗦𝗘**

🇬🇧 English      → `english`  
🇫🇷 French       → `french`  
🇳🇬 Yoruba       → `yoruba`  
🇳🇬 Hausa        → `hausa`  
🇪🇸 Spanish      → `spanish`  
🇩🇪 German       → `german`  
🇮🇹 Italian      → `italian`  
🇯🇵 Japanese     → `japanese`  
🇨🇳 Chinese      → `chinese`  
🇷🇺 Russian      → `russian`  
🇰🇷 Korean       → `korean`

✏️ *Usage:*  
Reply to any message and type:  
`.translate english`
"""
        await event.reply(languages, parse_mode="md")
        return

    if not event.is_reply:
        await event.reply("⚠️ Please reply to the message you want to translate.")
        return

    try:
        reply_msg = await event.get_reply_message()
        text = reply_msg.message
        translator = Translator()
        translated = translator.translate(text, dest=lang.lower())

        await event.reply(f"✅ **Translated to {lang.capitalize()}**:\n\n`{translated.text}`", parse_mode="md")

    except Exception as e:
        await event.reply(f"❌ Error: {e}")
        

#

# ✅ Supported emojis
all_emojis = [
    "😂", "❤️", "🔥", "👍", "👎", "💯", "🥰", "😢", "😡", "👏",
    "🎉", "🤔", "🤯", "💀", "😈", "😎", "🤖", "😬", "🥶", "🤡",
    "😳", "🤑", "💩", "🤮", "🫡", "😭", "😇", "😍", "😤", "🫠"
]

# 📥 Turn ON autoreact
@client.on(events.NewMessage(pattern=r"\.autoreact on"))
async def enable_autoreact(event):
    global auto_react_enabled
    auto_react_enabled = True
    await event.reply("✅ Auto-reaction is now **ON**!")

# 📴 Turn OFF autoreact
@client.on(events.NewMessage(pattern=r"\.autoreact off"))
async def disable_autoreact(event):
    global auto_react_enabled
    auto_react_enabled = False
    await event.reply("🚫 Auto-reaction is now **OFF**.")

# 💬 React to all messages
@client.on(events.NewMessage(incoming=True))
async def react_to_messages(event):
    global auto_react_enabled
    if not auto_react_enabled:
        return
    try:
        # ✅ Skip self-messages
        if event.sender_id == (await client.get_me()).id:
            return

        # 🎲 Random emoji
        emoji = random.choice(all_emojis)

        # 💬 React
        await client(functions.messages.SendReactionRequest(
            peer=event.chat_id,
            msg_id=event.id,
            reaction=[types.ReactionEmoji(emoticon=emoji)],
            big=True
        ))

    except Exception as e:
        print(f"⚠️ Auto-reaction error: {e}")
        
        
@client.on(events.NewMessage(pattern=r"\.pp(?:\s+@?(\w+))?"))
async def get_pp(event):
    username = event.pattern_match.group(1)

    try:
        if username:
            user = await client.get_entity(username)
        elif event.is_reply:
            reply_msg = await event.get_reply_message()
            user = await client.get_entity(reply_msg.sender_id)
        else:
            user = await client.get_entity(event.sender_id)

        photos = await client.get_profile_photos(user)

        if photos.total == 0:
            await event.reply("❌ User has no profile photo.")
            return

        await client.send_file(event.chat_id, photos[0], caption=f"📸 Profile picture of [{user.first_name}](tg://user?id={user.id})", parse_mode="md")

    except Exception as e:
        await event.reply(f"❌ Failed to get profile picture:\n`{str(e)}`")

@client.on(events.NewMessage(pattern=r"\.linkgc"))
async def link_gc(event):
    if not event.is_group:
        await event.reply("❌ This command can only be used in group chats.")
        return

    try:
        result = await client(ExportChatInviteRequest(event.chat_id))
        await event.reply(f"🔗 **Group Link:**\n{result.link}")
    except Exception as e:
        await event.reply(f"⚠️ Failed to get group link:\n`{e}`")
        
pickup_lines = [
    "Are you a magician? Because whenever I look at you, everyone else disappears. ✨",
    "Do you have a map? I just got lost in your eyes. 😍",
    "Is your name Google? Because you have everything I’ve been searching for. 🔍❤️",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you. 💔➡️❤️",
    "If beauty were time, you’d be eternity. ⏳",
    "Are you French? Because Eiffel for you. 🇫🇷💕",
    "Are you made of copper and tellurium? Because you’re Cu-Te. 🧪",
    "Do you like raisins? How do you feel about a date? 😏",
    "I must be a snowflake, because I’ve fallen for you. ❄️❤️",
    "If I could rearrange the alphabet, I’d put U and I together. 🔤💘"
]



@client.on(events.NewMessage(pattern=r"\.get$"))
async def get_chat_photo(event):
    chat = await event.get_input_chat()
    try:
        photo = await client.download_profile_photo(chat)
        if photo:
            await event.reply(file=photo, message="📷 Here's the profile picture of this chat.")
            os.remove(photo)  # Clean up the downloaded file
        else:
            await event.reply("⚠️ This chat has no profile picture.")
    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")
        
@client.on(events.NewMessage(pattern=r"\.pickup"))
async def pickup_handler(event):
    line = random.choice(pickup_lines)
    await event.reply(f"💘 {line}")
    
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def uptime_handler(event):
    current_time = time.time()
    uptime = int(current_time - start_time)

    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)

    await event.reply(
        f"🟢 **Bot Uptime:**\n"
        f"`{hours}h {minutes}m {seconds}s`"
    )
   
@client.on(events.NewMessage(pattern=r"\.toimage$"))
async def sticker_to_jpeg(event):
    from PIL import Image
    import subprocess
    import os

    reply = await event.get_reply_message()

    if not reply or not reply.sticker:
        return await event.reply("❌ Reply to a sticker to convert it to JPEG.")

    try:
        # Download the sticker
        file_path = await client.download_media(reply.media)
        file_ext = os.path.splitext(file_path)[1].lower()
        output_path = file_path.replace(file_ext, ".jpg")

        # Convert webp (static sticker)
        if file_ext == ".webp":
            img = Image.open(file_path).convert("RGB")
            img.save(output_path, "JPEG")

        # Convert tgs (animated sticker)
        elif file_ext == ".tgs":
            png_path = file_path.replace(".tgs", ".png")
            cmd = f"lottie_convert.py {file_path} {png_path}"
            os.system(cmd)
            img = Image.open(png_path).convert("RGB")
            img.save(output_path, "JPEG")
            os.remove(png_path)

        # Convert webm (video sticker)
        elif file_ext == ".webm":
            cmd = f"ffmpeg -i {file_path} -vf 'select=eq(n\\,0)' -q:v 3 {output_path}"
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        else:
            return await event.reply(f"⚠️ Unsupported sticker format: `{file_ext}`")

        await event.reply("🖼 Sticker converted Powered by Nagato X drenox:", file=output_path)

        os.remove(file_path)
        os.remove(output_path)

    except Exception as e:
        await event.reply(f"❌ Error: {e}")
    
@client.on(events.NewMessage(pattern=r'\.game'))
async def game_menu(event):
    await event.reply(
        "**🎮 Game Center Menu 🎮**\n\n"
        "Choose a game to play:\n"
        "1️⃣ X and O — Type `.play xo`\n"
        "2️⃣ Police Chase — Type `.play police`\n"
        "3️⃣ Guess the Number — Type `.play guess`\n"
        "4️⃣ Rock Paper Scissors — Type `.play rps`\n"
        "\n💡 Use `.play <game_name>` to start!"
    )
    
@client.on(events.NewMessage(pattern=r'\.play xo'))
async def tictactoe(event):
    board = ["⬜"] * 9
    message = "**🎮 X and O Game (Tic Tac Toe)**\n\n"
    message += "Use the numbers 1-9 to choose your move:\n\n"
    message += f"{board[0]} {board[1]} {board[2]}\n{board[3]} {board[4]} {board[5]}\n{board[6]} {board[7]} {board[8]}\n"
    message += "\n📝 Game not interactive yet. Just a demo."

    await event.reply(message)
    
active_battles = {}

# Word list (you can expand this)
words = ["python", "telegram", "userbot", "drenox", "nagato", "battle", "fast", "game", "winner", "typing"]

@client.on(events.NewMessage(pattern=r"\.speedgame"))
async def start_type_battle(event):
    chat_id = event.chat_id

    if chat_id in active_battles:
        await event.reply("⏳ A battle is already in progress!")
        return

    word = random.choice(words)
    active_battles[chat_id] = word

    await event.reply(f"⚔️ TYPE BATTLE STARTED!\n\nFirst to type:\n{word}")

    try:
        # Wait for the correct word
        @client.on(events.NewMessage(chats=chat_id))
        async def battle_listener(msg):
            if msg.raw_text.strip().lower() == word.lower():
                await msg.reply(f"🏆 {msg.sender.first_name} typed it first! The word was {word}.")
                del active_battles[chat_id]
                client.remove_event_handler(battle_listener, events.NewMessage)
        
        # Allow game to expire in 30 seconds
        await asyncio.sleep(30)
        if chat_id in active_battles:
            await event.reply(f"⌛ Time's up! No one typed {word} correctly.")
            del active_battles[chat_id]
            client.remove_event_handler(battle_listener, events.NewMessage)

    except Exception as e:
        if chat_id in active_battles:
            del active_battles[chat_id]
        await event.reply("⚠️ An error occurred. Battle cancelled.")
        
snake_games = {}  # chat_id: game_state

GRID_SIZE = 5
OBSTACLE_COUNT = 4

def gen_empty_grid():
    return [["▫️"] * GRID_SIZE for _ in range(GRID_SIZE)]

def place_random_empty(grid):
    while True:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if grid[y][x] == "▫️":
            return x, y

def render_grid(grid):
    return "\n".join(["".join(row) for row in grid])

@client.on(events.NewMessage(pattern=r"\.snake\s+@(\w+)"))
async def start_snake_game(event):
    opponent_username = event.pattern_match.group(1)
    chat_id = event.chat_id
    sender = await event.get_sender()
    opponent = await client.get_entity(opponent_username)

    if chat_id in snake_games:
        await event.reply("🐍 A Snake Duel is already in progress!")
        return

    grid = gen_empty_grid()

    # Place player A and B
    a_x, a_y = 0, 0
    b_x, b_y = GRID_SIZE - 1, GRID_SIZE - 1
    grid[a_y][a_x] = "🐍A"
    grid[b_y][b_x] = "🐍B"

    # Place apple
    apple_x, apple_y = place_random_empty(grid)
    grid[apple_y][apple_x] = "🍎"

    # Place obstacles
    for _ in range(OBSTACLE_COUNT):
        ox, oy = place_random_empty(grid)
        grid[oy][ox] = "🧱"

    snake_games[chat_id] = {
        "players": [sender.id, opponent.id],
        "positions": {sender.id: (a_x, a_y), opponent.id: (b_x, b_y)},
        "scores": {sender.id: 0, opponent.id: 0},
        "apple": (apple_x, apple_y),
        "turn": sender.id,
        "grid": grid,
        "message": None
    }

    board = render_grid(grid)
    await event.reply(f"🐍 Snake Duel Started Between {sender.first_name} and {opponent.first_name}!\n\n{board}\n\n{sender.first_name}'s turn — use .move up/down/left/right")

@client.on(events.NewMessage(pattern=r"\.move (up|down|left|right)"))
async def move_player(event):
    chat_id = event.chat_id
    sender_id = event.sender_id

    if chat_id not in snake_games:
        return

    game = snake_games[chat_id]
    if sender_id != game["turn"]:
        return  # Not your turn

    direction = event.pattern_match.group(1)
    grid = game["grid"]
    x, y = game["positions"][sender_id]

    # Remove current snake symbol
    grid[y][x] = "▫️"

    new_x, new_y = x, y
    if direction == "up":
        new_y = max(0, y - 1)
    elif direction == "down":
        new_y = min(GRID_SIZE - 1, y + 1)
    elif direction == "left":
        new_x = max(0, x - 1)
    elif direction == "right":
        new_x = min(GRID_SIZE - 1, x + 1)

    cell = grid[new_y][new_x]

    if cell == "🧱":
        # Hit obstacle
        grid[y][x] = "🐍A" if sender_id == game["players"][0] else "🐍B"
        await event.reply("🚫 You hit a wall (🧱)! Try a different direction.")
        return

    # Check apple
    if (new_x, new_y) == game["apple"]:
        game["scores"][sender_id] += 1
        apple_x, apple_y = place_random_empty(grid)
        game["apple"] = (apple_x, apple_y)
        grid[apple_y][apple_x] = "🍎"

        if game["scores"][sender_id] >= 3:
            winner = (await client.get_entity(sender_id)).first_name
            del snake_games[chat_id]
            await event.reply(f"🏆 {winner} wins the Snake Duel!")
            return

    # Place new position
    symbol = "🐍A" if sender_id == game["players"][0] else "🐍B"
    grid[new_y][new_x] = symbol
    game["positions"][sender_id] = (new_x, new_y)

    # Switch turn
    game["turn"] = game["players"][1] if sender_id == game["players"][0] else game["players"][0]
    next_player = await client.get_entity(game["turn"])

    board = render_grid(grid)
    await event.reply(f"{board}\n\nNow it's {next_player.first_name}'s turn — use .move up/down/left/right")
    
@client.on(events.NewMessage(pattern=r"\.autoreply (on|off)"))
async def toggle_autoreply(event):
    global auto_reply_enabled
    if event.is_private:
        if event.pattern_match.group(1) == "on":
            auto_reply_enabled = True
            await event.reply("✅ Auto-reply has been turned ON.")
        else:
            auto_reply_enabled = False
            await event.reply("❌ Auto-reply has been turned OFF.")
            
@client.on(events.NewMessage(incoming=True))
async def auto_reply_handler(event):
    global auto_reply_enabled
    if event.is_private and auto_reply_enabled and not await client.is_user_authorized():
        # Replace the message below with anything you want
        await event.reply("👋 Hello there! My boss is currently offline. Please leave a message.")
        
@client.on(events.NewMessage(pattern=r"\.owner"))
async def owner_handler(event):
    if event.sender_id != 123456789:  # 🔑 Replace with your Telegram user ID
        return await event.reply("❌ You are not authorized to use this command.")
    
    message = f"""
🤖 **Bot Owner Details**

👤 Name: Lord Nagato The Alpha
🔗 Username: @Officailnagato_1
💬 Status: Active Developer of Reaper X MD
"""
    await event.reply(message)
    
@client.on(events.NewMessage(pattern=r"\.channel"))
async def channel_handler(event):
    channel_username = "@YourChannelUsername"  # Replace with your channel's username
    channel_name = "Your Channel Name"  # Replace with your channel's name
    channel_description = "This is a description of the channel. Share updates, news, and more!"  # Optional

    message = f"""
🤖 **Channel Info**

📢 **Officailnagatotech**: {channel_name}
🔗 **https://t.me/+ylcFxv1lARkxMDZk**
:**https://t.me/thetailungtech**

📝 **fuck woman and fall in love with tech **: {channel_description}
"""
    await event.reply(message)
    
    
@client.on(events.NewMessage(pattern=r"\.tagall(?: (.+))?"))
async def tag_all(event):
    if not event.is_group:
        await event.reply("❌ This command can only be used in group chats.")
        return

    message = event.pattern_match.group(1) or "Hey everyone!"
    chat = await event.get_input_chat()

    tagged_users = []
    count = 1
    async for user in client.iter_participants(chat, filter=ChannelParticipantsSearch("")):
        if user.username:
            tagged_users.append(f"{count}. @{user.username}")
            count += 1
        elif user.first_name:
            tagged_users.append(f"{count}. [{user.first_name}](tg://user?id={user.id})")
            count += 1

    MAX_MESSAGE_LENGTH = 4000
    chunk = f"📢 {message}\n\n"
    chunks = []

    for tag in tagged_users:
        if len(chunk) + len(tag) + 2 > MAX_MESSAGE_LENGTH:
            chunks.append(chunk)
            chunk = ""
        chunk += tag + "\n"

    if chunk:
        chunks.append(chunk)

    for chunk in chunks:
        await event.reply(chunk, link_preview=False)

# 🟥 Step 4: Start the bot

print("🤖 Starting Reaper X bot....")
client.start()
client.run_until_disconnected()