# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25229804"))
API_HASH = getenv("API_HASH", "c01077936d5a4e7b466657f19b795848")
BOT_TOKEN = getenv("BOT_TOKEN", "7135879547:AAHIg95dPz65F5jhh6PFeHXKGb2qaW_LAiA")
OWNER_ID = int(getenv("OWNER_ID", "6471015271"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://avi12839:avi7675754@cluster0.cowrqxq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002004344915"))
FORCESUB = getenv("FORCESUB", "malikhoaap")
