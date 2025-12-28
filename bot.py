# ---------------------------------------------------
# File Name: Q5.2.py
# Author: MyselfNeon
# Original Repo: https://github.com/MyselfNeon/SaveRestrictions-Bot
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# ---------------------------------------------------

import asyncio
import importlib
import gc
import datetime
from datetime import timezone, timedelta
from pyrogram import idle
from MyselfNeon.modules import ALL_MODULES
from MyselfNeon.core.mongo.plans_db import check_and_remove_expired_users
from aiojobs import create_scheduler
from MyselfNeon import app
from config import LOG_GROUP

# --- Bot-Start ---
loop = asyncio.get_event_loop()

# --- Function to schedule expiry checks ---
async def schedule_expiry_check():
    scheduler = await create_scheduler()
    while True:
        await scheduler.spawn(check_and_remove_expired_users())
        await asyncio.sleep(60)  # Check every hour
        gc.collect()

async def neon_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("MyselfNeon.modules." + all_module)
    print("""
--------------------------------------------
📂 Bot Deployed successfully ...
👨‍💻 Author: MyselfNeon
🌐 GitHub: https://github.com/MyselfNeon/
📬 Telegram: https://t.me/neonfiles
🗓️ Created: 2025-12-11
🛠️ Version: 2.0.8
📜 License: MIT License
--------------------------------------------
""")

    asyncio.create_task(schedule_expiry_check())
    print("Auto removal started ...")
    
    try:
        # ✅ Indian Standard Time
        IST = timezone(timedelta(hours=5, minutes=30))

        # Bot startup log
        now = datetime.datetime.now(IST)
        date = now.strftime("%d/%m/%y")
        time = now.strftime("%I:%M:%S %p")
        
        # Get Bot Info
        me = await app.get_me()
        
        # Construct the restart message
        restart_msg = (
            f"**⌬ Restarted Successfully !**\n"
            f"**┟ Bot:** __{me.first_name} (@{me.username})__\n"
            f"**┟ Date:** __{date}__\n"
            f"**┠ Time:** __{time}__\n"
            f"**┠ TimeZone:** __Asia/Kolkata__\n"
            f"**┖ Version:** __v2.0.8-x__"
        )
        
        await app.send_message(int(LOG_GROUP), restart_msg)
    except Exception as e:
        print(f"Failed to send restart log: {e}")

    await idle()
    print("Bot stopped...")

if __name__ == "__main__":
    loop.run_until_complete(neon_boot())

# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
