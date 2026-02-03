<h2 align="center"><i>Save Restricted Bot</i></h1>
<p align="center">
  <a href="[https://t.me/SaveRestriction_oBot](https://t.me/SaveRestriction_oBot)">
    <img src="[https://files.catbox.moe/krxuel.jpg](https://files.catbox.moe/krxuel.jpg)" alt="Cover Image" width="550">
  </a>
</p>  
  <p align="center">
   </strong></a>
    <br><b>
    <a href="[https://github.com/MyselfNeon/SaveRestricted/issues](https://github.com/MyselfNeon/SaveRestricted/issues)"><i>Report a Bug or Request Feature</i></a></b>
  </p>

#### *About ➠*

<p align="center">
    <a href="[https://github.com/MyselfNeon/SaveRestricted](https://github.com/MyselfNeon/SaveRestricted)">
        <img src="[https://img.icons8.com/fluency/96/telegram-app.png](https://img.icons8.com/fluency/96/telegram-app.png)" height="100" width="100" alt="Logo">
    </a>
</p>
<p align='center'>
  <i><b>This Bot allows you to Download and Save Restricted Content (Text, Media, Files) from Public & Private Channels directly to your Chat. It supports Session Login, Verification System, and Bulk Downloading.</b></i>
</p>


#### *How To Deploy ➠*

<details><summary><b><i>Deploy on Multiple Servers</i></summary></b></summary>
<br>
<details>
    <summary><b><i>Deploy on Heroku (Free/Paid)</i></b></summary>
    <br>

  * ***Fork This Repo***
  * ***Click on Deploy Easily***
  * ***Press the below Button to Fast Deploy on Heroku***

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)]([https://heroku.com/deploy](https://heroku.com/deploy))

  * ***Go to <a href="#config-variables-">Variables Tab</a> for more info on Setting up Environmental Variables.***
  </details>

<details>
  <summary><b><i>Deploy Using Docker</i></b></summary>
<br>

* ***Clone the Repository :***
```sh
git clone https://github.com/MyselfNeon/SaveRestricted
cd SaveRestricted
```

* ***Build own Docker Image :***
```sh
docker build -t saverestricted .
```

* ***Create ENV and Start Container :***
```sh
docker run -d --restart unless-stopped --name saverestricted \
-v /PATH/TO/.env:/app/.env \
saverestricted
```
</details>

<details>
    <summary><b><i>Deploy Locally</i></b></summary>
    <br>

  ```sh
  git clone https://github.com/MyselfNeon/SaveRestricted
  cd SaveRestricted
  python3 -m venv ./venv
  . ./venv/bin/activate
  pip install -r requirements.txt
  python3 bot.py
  ```

  * ***To stop the Bot Press <kbd>CTRL</kbd> + <kbd>C</kbd>.***

  * ***If you want to run this Bot 24/7 on a VPS, follow these Steps :***
  ```sh
  sudo apt install tmux -y
  tmux
  python3 bot.py
  ```
  * ***Now you can Close the VPS terminal — the Bot will Keep Running in the Background.***

  </details>

</details>

#### *Config Variables ➠*

<details><summary><b><i>ENV Variables</i></summary></b></summary>

#### *Mandatory Variables ➠*

* [`API_ID`]: ***From [My Telegram](https://my.telegram.org). `int`***
* [`API_HASH`]: ***From [My Telegram](https://my.telegram.org). `str`***
* [`BOT_TOKEN`]: ***Telegram API Bot Token, Get it from [@BotFather](https://t.me/BotFather). `str`***
* [`ADMINS`]: ***Your Telegram User ID (For Admin Commands). `int`***
* [`DB_URI`]: ***[MongoDB URI](https://cloud.mongodb.com) for Saving User Sessions and Verification Data. `str`***
* [`LOG_CHANNEL`]: ***ID of the Channel where Bot will send Logs of New Users (Start with -100). `int`***
* [`DUMP_CHANNEL`]: ***ID of the Channel to Dump all Leeched Files with User Info (Start with -100). `int`***

#### 🪐 *Optional Variables* :

* [`START_PIC`]: ***To set Image at `/start` Command. Defaults to Pre-Set image. `str`***
* [`ERROR_MESSAGE`]: ***Set True if you want Error Logs in PM. Defaults `True`. `bool`***

#### 🔐 *Verification Variables* :

* [`VERIFY`]: ***Set `True` to Enable Verification System. `bool`***
* [`VERIFY_SHORTLINK_URL`]: ***Your Shortener Domain (e.g., `ShrinkMe.io`). `str`***
* [`VERIFY_SHORTLINK_API`]: ***Your Shortener API Key. `str`***
* [`VERIFY_TUTORIAL`]: ***Link to a Tutorial Video/Post on how to verify. `str`***

</details>
 
#### *Bot Commands ➠* 

<details><summary><b><i>Bot Commands</i></b></summary>
  
```
start - Check if Bot is Alive
help - Get Help Message
login - Login via Session String
logout - Logout Current Session
verify - Verify to get 4 Hours Access
cancel - Cancel Ongoing Batch Process
broadcast - Broadcast Message to Users [ADMIN]
users - Get List of All Users [ADMIN]
restart - Restart the Bot [ADMIN]
```
<b><i>⪼ Copy all Commands and paste it in <a href='[https://t.me/botfather](https://t.me/botfather)'>BotFather</a> to apply Commands.

</details>

#### *Usage Guide ➠*

<details><summary><b><i>How to Use</i></b></summary>

***1. Public Posts***
> Just send the link: `https://t.me/Channel/123`

***2. Private Chats***
> First `/login`, then send link: `https://t.me/c/12345/678`

***3. Batch Mode***
> Send range: `https://t.me/Channel/100-120`

***4. Bot Chats***
> Use format: `https://t.me/b/BotUser/123`

</details>

#### Contact Developer 👨‍💻

[![Contact Developer](https://img.shields.io/badge/Contact-Developer-blue?logo=telegram)](https://t.me/MyselfNeon)    
[![Telegram Channel](https://img.shields.io/badge/Telegram-Main%20Channel-blue?logo=telegram)](https://t.me/neonfiles)  
Join My <a href='[https://t.me/neonfiles](https://t.me/neonfiles)'>Update Channel</a> For More Update Regarding Repo.

#### *Thanks To ➠* ❤️
 - <b>Thanks To [Neon An](https://t.me/MyselfNeon) To Modify And Add Amazing Features
 - Thanks To Everyone who have Contributed In This Repo ❤️</b>

---
<h4 align="center">➠ © <a href="[https://myselfneon.github.io/neon/](https://myselfneon.github.io/neon/)" target="_blank" rel="noopener noreferrer">MyselfNeon 🍟</a></h4>