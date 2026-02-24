# ---------------------------------------------------
# File Name: App.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# Created: 2025-11-21
# Last Modified: 2025-11-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <body style="background-color:black; color:#39FF14; display:flex; justify-content:center; align-items:flex-start; height:100vh; margin:0; font-family:sans-serif; padding-top:20vh; font-size:4rem;">
        Coded By @MyselfNeon
    </body>
    """

if __name__ == "__main__":
    app.run()


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles        )
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
