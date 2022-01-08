import os
from pyrogram import Client

TRIGGERS ="/"
API_HASH = "6bb0682b4af56456201c3b9d8b99c94a"
BOT_TOKEN = "2025919134:AAGAyAXR9hTJZu6v75-5ho8ao95mcppXacU"
BOT_NAME = "@Yukinonthecutebot"
DB_URL = "mongodb+srv://TROJ3N:Nethika123@cluster0.uppg6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
ANILIST_CLIENT = "TROJ3N"
ANILIST_SECRET = "KyiaqDvE9FyT0epLJyKXhQQx3IsPPFmMOQWE6YNM"
ANILIST_REDIRECT_URL = "https://t.me/waifuNetwork"
API_ID = "4091096"
LOG_CHANNEL_ID = "1954364940"
OWNER = list(filter(lambda x: x, map(int, os.environ.get("OWNER_ID", "").split())))

DOWN_PATH = "anibot/downloads/"
HELP_DICT = dict()

plugins = dict(root="anibot/plugins")
anibot = Client("anibot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=plugins)

has_user: bool = False
if os.environ.get('USER_SESSION'):
    has_user: bool = True
    user = Client(os.environ.get('USER_SESSION'), api_id=API_ID, api_hash=API_HASH)

HELP_DICT['Misc'] = '''

'''

HELP_DICT["Additional"] = """
"""

HELP_DICT["Anilist"] = """

"""

HELP_DICT["Oauth"] = """

"""
