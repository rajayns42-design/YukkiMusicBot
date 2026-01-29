#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Database to save your chats and stats
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Duration Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Anshika Music Bot")

# Your User ID.
OWNER_ID = list(map(int, getenv("OWNER_ID", "8211189367").split()))

# Heroku Config
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# Repositories
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rajayns42-design/YukkiMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support Links
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Love_Bot_143")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Love_Ki_Duniyaa")

# Assistant Settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Downloader Settings
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# External Links
GITHUB_REPO = getenv("GITHUB_REPO", None)
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Limits
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

# File Size Limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

# Commands Setup
SET_CMDS = getenv("SET_CMDS", False)

# String Sessions
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Internal Vars
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []

# ==========================================
# 🔥 AAPKI NAYI IMAGES (Yukki Format)
# ==========================================

HELP_IMG_URL = getenv("HELP_IMG_URL", "https://i.ibb.co/xPjc7tv/help-menu.jpg")
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/0ob0k3.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/26nzoq.jpg")

PLAYLIST_IMG_URL = "https://files.catbox.moe/f2s4ws.jpg"
STATS_IMG_URL = "https://telegra.ph/file/default_image.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
GLOBAL_IMG_URL = "https://files.catbox.moe/0ob0k3.jpg"

# ==========================================

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

# Repo & Channel Validation
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        sys.exit("[ERROR] - SUPPORT_CHANNEL url is wrong.")

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        sys.exit("[ERROR] - SUPPORT_GROUP url is wrong.")

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        sys.exit("[ERROR] - UPSTREAM_REPO url is wrong.")
