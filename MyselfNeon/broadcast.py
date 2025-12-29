# ---------------------------------------------------
# File Name: Broadcast.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyselfNeon
# YouTube: https://youtube.com/@MyselfNeon
# Created: 2025-10-21
# Last Modified: 2025-10-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
from database.db import db
from pyrogram import Client, filters
from config import ADMINS
import asyncio
import datetime
import time
from pyrogram.types import Message, BotCommand
import json
import os
import sys

# ---------------------------------------------------
# Broadcast helper function
# ---------------------------------------------------
async def broadcast_messages(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await db.delete_user(int(user_id))
        return False, "Deleted"
    except UserIsBlocked:
        await db.delete_user(int(user_id))
        return False, "Blocked"
    except PeerIdInvalid:
        await db.delete_user(int(user_id))
        return False, "Error"
    except Exception as e:
        print(f"[!] Broadcast error for {user_id}: {e}")
        return False, "Error"

# ---------------------------------------------------
# /broadcast command
# ---------------------------------------------------
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast_command(bot: Client, message: Message):
    b_msg = message.reply_to_message
    if not b_msg:
        return await message.reply_text(
            "**__Reply to this command with the message you want to broadcast.__**",
            quote=True
        )

    users = await db.get_all_users()
    sts = await message.reply_text(
        text='**__Broadcasting your message...__**',
        quote=True
    )

    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed = 0
    success = 0

    async for user in users:
        user_id = user.get('id')
        if user_id:
            pti, sh = await broadcast_messages(int(user_id), b_msg)
            if pti:
                success += 1
            else:
                if sh == "Blocked":
                    blocked += 1
                elif sh == "Deleted":
                    deleted += 1
                elif sh == "Error":
                    failed += 1
            done += 1

            if done % 20 == 0:
                await sts.edit(
                    f"**__Broadcast In Progress:__**\n\n"
                    f"**👥 Total Users:** {total_users}\n"
                    f"**💫 Completed:** {done} / {total_users}\n"
                    f"**✅ Success:** {success}\n"
                    f"**🚫 Blocked:** {blocked}\n"
                    f"**🚮 Deleted:** {deleted}"
                )
        else:
            done += 1
            failed += 1
            if done % 20 == 0:
                await sts.edit(
                    f"**__Broadcast In Progress:__**\n\n"
                    f"**👥 Total Users:** {total_users}\n"
                    f"**💫 Completed:** {done} / {total_users}\n"
                    f"**✅ Success:** {success}\n"
                    f"**🚫 Blocked:** {blocked}\n"
                    f"**🚮 Deleted:** {deleted}"
                )

    time_taken = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts.edit(
        f"**__Broadcast Completed:__**\n"
        f"**⏰ Completed in:** {time_taken}\n\n"
        f"**👥 Total Users:** {total_users}\n"
        f"**💫 Completed:** {done} / {total_users}\n"
        f"**✅ Success:** {success}\n"
        f"**🚫 Blocked:** {blocked}\n"
        f"**🚮 Deleted:** {deleted}"
    )

# ---------------------------------------------------
# /users Command (Standalone + JSON export)
# ---------------------------------------------------
@Client.on_message(filters.command("users") & filters.user(ADMINS))
async def users_count(bot: Client, message: Message):
    msg = await message.reply_text("⏳ <b>__Gathering User Data...__</b>", quote=True)
    try:
        total = await db.total_users_count()
        await msg.edit_text(
            f"""
🌀 <b><i>User Analytics Update</i></b> 🌀

👥 <b>Total Registered Users:</b> {total}
🛰 <b>System Status:</b> Active ✅
🧠 <b>Data Source:</b> MongoDB (async)
"""
        )

        users_cursor = await db.get_all_users()
        users_list = []
        async for user in users_cursor:
            users_list.append({
                "name": user.get("name", "None"),
                "username": user.get("username", "None"),
                "id": user.get("id")
            })

        tmp_path = "SaveRestricted.json"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(users_list, f, indent=2, ensure_ascii=False)

        caption = f"📄 **Recorded {len(users_list)} Users**"
        await message.reply_document(
            document=tmp_path,
            caption=caption
        )

        try:
            os.remove(tmp_path)
        except Exception as e:
            print(f"[!] Failed to Delete File {tmp_path}: {e}")

    except Exception as e:
        await msg.edit_text(f"**__⚠️ Error Fetching User Data:__**\n<code>{e}</code>")
        print(f"[!] /users error: {e}")

# --- Set Commands ---
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

# Credits
# Developer Telegram: @MyselfNeon
# Update channel: @NeonFiles