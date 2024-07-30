# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "27526328"))
	API_HASH = os.environ.get("API_HASH", "db231e73712db0b6397f624a75a760f8")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", " 6791224524:AAHdWd5lTOBZzZqVI3duDRPfejIzdkgtr4E")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Cholefilestorebot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001941319109"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "7102263732"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Anivoid:akhand1616@cluster05.kzyifsq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster05")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002088432628")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "1582227872").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/Cholefilestorebot)
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Aries](https://t.me/Ariesaep) 
│
├🔹 **Bot Support:** [Support Group](https://t.me/Team_Roku)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/Rokubotz)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@Ariesaep](https://github.com/Anivoid/chole-file-store)
 
 I am Super noob Please Support My Hard Work.

[Donate Me]() or ``````
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
