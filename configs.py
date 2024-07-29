# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "27526328"))
	API_HASH = os.environ.get("API_HASH", "db231e73712db0b6397f624a75a760f8")
	BOT_TOKEN = os.environ.get("BOT_TOKEN","7466292166:AAGDfvvC7RTeCYRnXjGwn2iv5sFL6JoOy-8")
	BOT_USERNAME = os.environ.get("BOT_USERNAME" , "haniflixfilestorebot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002213717760"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "Ariesaep"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Animeverse07:shubh07@cluster0.i7z8kjh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002149638793")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/haniflixfilestorebot)
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [waifu](https://t.me/waifuae) 
│
├🔹 **Bot Support:** [Support Group](https://t.me/animesilvervoid)
│
├🔸 **Bot Updates:** [haniflix](https://t.me/Haniflix)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@PredatorHackerzZ](https://github.com/PredatorHackerzZ)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/DonateXrobot) or ```teleroidgroup@axl```
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
