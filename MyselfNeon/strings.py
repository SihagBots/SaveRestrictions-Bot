# ---------------------------------------------------
# File Name: Strings.py
# Author: NeonAnurag
# Original Repo: https://github.com/MyselfNeon/SaveRestrictions-Bot
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# ---------------------------------------------------

import os
import sys
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, BotCommand
from config import ADMINS

HELP_TXT = """<b>=====  🆘 𝐇𝐄𝐋𝐏 𝐌𝐄𝐍𝐔 🆘  =====</b>

<blockquote><b>‣ <i>For Private Chats</i></b></blockquote>
<i>First Send The Invite Link Of The Chat</i>  
<i>(Unnecessary If The String Session Account Is Already A Member).</i>  
<i>Then Send The Post(S) Link.</i>  

<blockquote><b>‣ <i>For Bot Chats</i></b></blockquote>
<i>Send The Link With /b/, The Bot's Username, And The Message ID.</i>  
<i>(You May Need An Unofficial Client To Get The Message ID).</i>  

<b><i>Example:</i></b>  
<i>https://t.me/b/botusername/4321</i>  

<blockquote><b><i>‣ Multi Posts</i></b></blockquote>
<i>Send Public/Private Post Links As Explained Above. For Multiple Post(s)</i>  
<i>Use The Format [Start - End] to Send Multiple Messages.</i>  

<b><i>Examples:</i></b>  
<i>https://t.me/xxxx/1001-1010</i>  
<i>https://t.me/c/xxxx/101-120</i>  

<b>⚠️ <i>Spaces In Between Don’t Matter.</i></b>
"""

COMMANDS_TEXT = """
start - 🚀 𝘊𝘩𝘦𝘤𝘬 𝘈𝘭𝘪𝘷𝘦 𝘚𝘵𝘢𝘵𝘶𝘴
verify - 🎲 𝘎𝘦𝘵 4 𝘏𝘰𝘶𝘳𝘴 𝘍𝘳𝘦𝘦 𝘈𝘤𝘤𝘦𝘴𝘴
help - ⁉️ 𝘏𝘰𝘸 𝘵𝘰 𝘜𝘴𝘦 𝘔𝘦
login - 🔑 𝘓𝘰𝘨𝘪𝘯 𝘠𝘰𝘶𝘳 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘚𝘦𝘴𝘴𝘪𝘰𝘯
logout - 🚪 𝘓𝘰𝘨𝘰𝘶𝘵 𝘠𝘰𝘶𝘳 𝘚𝘦𝘴𝘴𝘪𝘰𝘯
cancel - ❌ 𝘊𝘢𝘯𝘤𝘦𝘭 𝘢𝘯𝘺 𝘖𝘯𝘨𝘰𝘪𝘯𝘨 𝘛𝘢𝘴𝘬
users - 👥 𝘊𝘩𝘦𝘤𝘬 𝘛𝘰𝘵𝘢𝘭 𝘜𝘴𝘦𝘳𝘴 (𝘈𝘥𝘮𝘪𝘯)
broadcast - 📢 𝘉𝘳𝘰𝘢𝘥𝘤𝘢𝘴𝘵 𝘔𝘴𝘨𝘴 𝘵𝘰 𝘜𝘴𝘦𝘳𝘴 (𝘈𝘥𝘮𝘪𝘯)
restart - 🔄 𝘙𝘦𝘴𝘵𝘢𝘳𝘵 𝘉𝘰𝘵 𝘚𝘦𝘳𝘷𝘦𝘳𝘴 (𝘈𝘥𝘮𝘪𝘯)
"""

# --- 1. RESTART COMMAND (Clean & Self-Contained) ---
@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_cmd(client: Client, message: Message):
    # 1. Send the confirmation message
    msg = await message.reply_text(
        "🔄 **__Restarting Bot...__**\n\n__Please wait while I reload...__"
    )
    
    await asyncio.sleep(100)
    
    await msg.delete()
    
    # 4. Restart the bot process
    os.execl(sys.executable, sys.executable, *sys.argv)

# --- 2. SET COMMANDS ---
@Client.on_message(filters.command("setcmd") & filters.user(ADMINS))
async def set_commands(client: Client, message: Message):
    commands = []
    
    for line in COMMANDS_TEXT.strip().split("\n"):
        if "-" in line:
            cmd, desc = line.split("-", 1)
            commands.append(BotCommand(cmd.strip(), desc.strip()))

    if not commands:
        return await message.reply_text("❌ No commands found.")

    try:
        await client.set_bot_commands(commands)
        await message.reply_text(f"✅ **__Success 🎉 \nUpdated {len(commands)} Commands.__**")
    except Exception as e:
        await message.reply_text(f"❌ **Error:** `{e}`")

# MyselfNeon
# # Don't Remove Credit 🥺
# # Telegram Channel @NeonFiles
