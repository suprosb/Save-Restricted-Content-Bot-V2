# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22920744"))
API_HASH = getenv("API_HASH", "31cb93c017f265e4fa6d0ba91236b826")
BOT_TOKEN = getenv("BOT_TOKEN", "7829774211:AAFRTIB9DzgBLtMV8K9s78nhFlX1MX0FNcQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5659668981").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://suproboiragi2:t4GwmmrWCkUcX3Ui@cluster0.nn4hh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002319340172")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002390556302"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
