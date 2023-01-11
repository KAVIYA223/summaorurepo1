import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "14569061"))
API_HASH = getenv("API_HASH", "27cdbce9ac58e83cec07e1147d9c9e05")

BOT_TOKEN = getenv("BOT_TOKEN", "5609170691:AAF_NuD3VX1u2B-64EsOskgDPbk1iIglbNc")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ammu:fradu@cluster0.h0nt8me.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001840160212"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "One Love Music")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5630946962 5695554322").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://t.me/king_of_izzy")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/melting_mooon")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Tamil_Buddies_Forever")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "999"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "cf6365361b7041b4a51036553acd9d4f")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "8b96133fe3d942faae5066be2f3cde91")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "9999"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "999999999"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQAs-59bHseDitWbUhDQIoLoNjKmBo5XcAyBk_R6K5RKWHgHK8FOP7jtZGUHvXpcdbh97zfNrKN619YnfwhCmqYZ5q3AScJmKeJZkSu80mSN747RT8RhO3XRaFeINtiX8F_krlQSSO7DGUYglZ_Ria-uh6M4O9Tg5y5QhIocIRvcLxBFz7RNANQBR8bfYr9LRmoE9UISVfQ217sv78bcufV59ZbtD7zspyYMZlyhaItH46eCKR01psEZDBjNRoUFdOAoRSNuKGQgk17uJPj9KrXYtXl7wLsZavsVNOR6M0I3cs4OxEEqrFTm4SjZZASXiCKhGt8gDd_rIQGJH1QweT_wAAAAAVpuM-YA")
STRING2 = getenv("STRING_SESSION2", "BQAdzOth1RABS6dX7wtjNSqyewE3uRa1YlhmSqPxcgeaDUbMnWJ0g76coH2GhN5deVQkbgRI6odb7V4T0KLyAl4jNVUWtx17HxcnWN9AGFjJx8oMqY4ersaH9-gG_YVvTIsj8WRtLxNuEK7yUW5iypG4SoLqaNoFU5jE7Idlfbqa7VgpeylKZemjzcLkdwGyxi4hzLjVgg6jyeVj1zbJ-sCJNVIWZQPn0L5zn98nmOtvg-zK_7sAXH9OlnxcS-LPZghA9rDd1MQLn9S4POmwvFGgVhLrEsZ4_ekWNXtk6AtmIV75B7yOleGzoU4tyue7UENhJlwv1a9DnBZuYlxZejCXAAAAATUG0NIA")
STRING3 = getenv("STRING_SESSION3", "BQBSo263ROuxZshJgPOFQYFDb2skdvKCqCk_QbX0qNXpCUHl9sE91lpV-4e5ernu4MznL4fDasK4fVSglrr_EFqwBvVVhJ5XleEPGh6FF9fp-6vUxRvqiXJkTTficer9TPL2QVzGIGnQD2m7kBSjVFIyMWeOcc-0uvTL-pxgdsmDLn_n0ZDNHOotUm9GhJHuxuPi1AcS_pN75gGiIwUbwFODVI1pM6K7wfOvcB384LrJfp6d5hyIYFyE5AMMq2H5qfPevo5Q7n8DqiYSaseQ1YG6f5J3w_YmcQv7BLHlqFJpN7jpkUo7pere5Xc11eV-fFqec_TyMLwOAo6Ae4ZiFk1tAAAAAWTumpYA")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/b91cca5b26f214e9193ed.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/077989b53c8c6d1c3f0b1.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/2f9e0afe8b621d0ae8791.jpg"

STATS_IMG_URL = "https://telegra.ph/file/5ef65010b3ad6cfb9d536.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


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


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/56d1760224589ee370186.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/56d1760224589ee370186.jpg"
