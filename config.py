import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "27282230"))
API_HASH = getenv("API_HASH", "215e34c9465c2719372d3d344533cd5d")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6836089486:AAGseEyMapwu-OSA69A8teu7EmGAAbz2lxk")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Moviesforyouworld:Moviesforyouworld@cluster0.0bf5qsv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "🌺 𝙈𝙤𝙤𝙣 ✘ 𝙈𝙪𝙨𝙞𝙘 🌺")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002014956416"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7165581725"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Karan9520/Awara-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MeAwaraHuu")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+YCzT3iL93dk3ZDVl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQGgSzYAsTyJXs8isKvjshuDe5YPd7VnCgpOeN4TO4DrlqbZZQkxE5SlC8CyI3ARW4GAxnOTYolMoE_trfzFBMrMFR_hfDWU2I3I6s40HvyeBWDV4nn2T4g8DTJfP9XvT87dc2UQMYutlGydFUaBJY3jLsKB8L6HczZUrBqX5VtRI2ZOc9vgRP2Hr-vJuKYvWu-88MQRAUOwFqH5vdtxT21pGb2-vmOX1lpgaAL93Hz9xhNPE-tP_nmCPOnllQUUi-ZhIVoI6uehdNiWY6s-csXzJhKmJqmSii8inIP9PsCx0iLo-9HILNvnqX4Kaga1vflF6fI3itlXlK5NVD78QdWkg8yNVgAAAAHNODlvAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/d6ca2536dfa8c212d42d6-8fc48a84faa43a4ab0.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/d6ca2536dfa8c212d42d6-8fc48a84faa43a4ab0.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/f2bdf974894c247a92b13-d818c8097da5669398.jpg"
STATS_IMG_URL = "https://graph.org/file/94f5d01499314aa5f0d2e-af69f2f980e0cb79a7.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/af9f68efcbd9891f409a1-825b1569cc81e950ce.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/f2093dee5ad35e5ea1746-267f1c370aa667e35f.jpg"
STREAM_IMG_URL = "https://graph.org/file/e3d83ef044282deb07c4d-84f7233dc4f7aba8d0.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/6735bb8fa411ac0f2077f-d144a1aaf93762ef04.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/3a1371f58388c955510c9-d7e12d85ca16b14e0a.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/3fa4726ac7ed75c14458d-5ea4995d76db809584.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/f7158ea1e22c33dacfbeb-7565f9a37a20210a18.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b6b9e9cbc969747840e58-b7c11d4ac68cce40bd.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
