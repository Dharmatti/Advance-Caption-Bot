from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "8096214375"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://envs.sh/Zh.jpg")
API_ID = int(getenv("API_ID", "22237124"))
API_HASH = str(getenv("API_HASH", "3ed92051ab8064684d8b1a5babd79ec8"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://auto:auto@cluster0.9qfo9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- @DVITTALKANNADAMOVIE `{file_name}`\n\n{file_size}</b>",
    )
)
