import re, os, time
import datetime


id_pattern = re.compile(r'^.\d+$') 


class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN", '6965002718:AAHMvGy52iR_K_cnJamRvf36NjU7SRPyfg8')

    SESSION_NAME = "links_money_converter_bot"

    API_ID = int(os.environ.get("API_ID", '25435105'))

    API_HASH = os.environ.get("API_HASH", '011126265844f2d7cc7dc1a024f6bc78')

    CLIENT_ID = os.environ.get("CLIENT_ID", '011126265844f2d7cc7dc1a024f6bc78')

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET", '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')

    BOT_OWNER = int(os.environ.get("BOT_OWNER", '6459102722'))

    BOT_START_TIME = time.time()
    
    BOT_START_DATETIME = datetime.datetime.now().strftime("%B %d, %Y %I:%M:%S %p")

    DB_NAME = os.environ.get("DB_NAME", "Utubeitbot")  

    DB_URL = os.environ.get("DB_URL")

    SUPPORT_CHAT_LINK = os.environ.get("SUPPORT_CHAT_LINK")

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "6459102722")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
