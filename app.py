# ---------------------------------------------------
# File Name: bot.py
# Modified For Koyeb Deployment
# ---------------------------------------------------

import sys
import os
import asyncio
import logging
import traceback
import logging.handlers as handlers
from datetime import datetime, timezone, timedelta

from aiohttp import web
from pyrogram import idle
import aiohttp

from FileStream.config import Telegram, Server, KEEP_ALIVE_URL
from FileStream.bot import FileStream
from FileStream.server import web_server
from FileStream.bot.clients import initialize_clients

# ------------------ Logging Setup ------------------

logging.basicConfig(
    level=logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(stream=sys.stdout),
        handlers.RotatingFileHandler(
            "streambot.log",
            mode="a",
            maxBytes=104857600,
            backupCount=2,
            encoding="utf-8"
        )
    ],
)

logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

# ------------------ Dynamic Port Fix ------------------

PORT = int(os.environ.get("PORT", 8080))  # Koyeb Auto Port
BIND_ADDRESS = "0.0.0.0"

# Override Server Config (important for Koyeb)
Server.PORT = PORT
Server.BIND_ADDRESS = BIND_ADDRESS

# ------------------ Server Setup ------------------

server = web.AppRunner(web_server())
loop = asyncio.get_event_loop()

# ------------------ Keep Alive ------------------

async def keep_alive():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await session.get(KEEP_ALIVE_URL)
                logging.info("Keep-alive ping sent.")
            except Exception as e:
                logging.error(f"Keep-alive failed: {e}")
            await asyncio.sleep(100)

# ------------------ Start Services ------------------

async def start_services():

    await FileStream.start()
    bot_info = await FileStream.get_me()

    FileStream.id = bot_info.id
    FileStream.username = bot_info.username
    FileStream.fname = bot_info.first_name

    # Start Clients
    await initialize_clients()

    # Start Web Server
    await server.setup()
    await web.TCPSite(server, BIND_ADDRESS, PORT).start()

    print("--------------------------------------------------")
    print(f" Bot Running => {bot_info.first_name}")
    print(f" Port => {PORT}")
    print("--------------------------------------------------")

    if KEEP_ALIVE_URL:
        loop.create_task(keep_alive())

    await idle()

# ------------------ Cleanup ------------------

async def cleanup():
    await server.cleanup()
    await FileStream.stop()

# ------------------ Main ------------------

if __name__ == "__main__":
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        pass
    except Exception:
        logging.error(traceback.format_exc())
    finally:
        loop.run_until_complete(cleanup())
        loop.stop()
        print("Bot Stopped")
