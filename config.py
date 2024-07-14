# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20152779"))
API_HASH = getenv("API_HASH", "703f6677b0a0797a11ab0476d66365d8")
BOT_TOKEN = getenv("BOT_TOKEN", "7048116321:AAF17Oe2QDsDNIXqhskpHx0HyrnaYUjazK4")
OWNER_ID = int(getenv("OWNER_ID", "6836834184"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002004344915"))
FORCESUB = getenv("FORCESUB", "malikhoaap")
