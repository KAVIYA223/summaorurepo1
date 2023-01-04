import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "14569061"))
API_HASH = getenv("API_HASH", "27cdbce9ac58e83cec07e1147d9c9e05")

BOT_TOKEN = getenv("BOT_TOKEN", "5609170691:AAF_NuD3VX1u2B-64EsOskgDPbk1iIglbNc")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ammu:fradu@cluster0.joy5eos.mongodb.net/?retryWrites=true&w=majority")
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

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "999999999"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQBYhWj9d8jOpMB-RcizNupR6ERDYRK5iUlYXeL0qqGR4pA-b7LTsFyYDyYbMV--1FffnhPIvP5SKYSxtlBaHitszZCE1dW1YRyGJu54vq12cXLZhpfS2OYAg0wluyr7g432mh-sC9T8DdziBM5F_P7AxeV40C4u0TVRBo7powr8EmEhHd3HktA8MMl-_e381XZF3zNk5lmbssgyKtMMiGTSfjm4GDbsYXnPHyoKW5csn9r_5y9aNkZ7zAdcZuRpayfll6Me6B-n5HPC0Bh4Fjjusxk63kNv-7sXji30nJGsk2RibHFrCuUq6bDt6Jpooyx13q3pbvug5kmWxpeTbVCCAAAAAVpuM-YA")
STRING2 = getenv("STRING_SESSION2", "BQCGgCtE7kSSvMMuJSzZ_quhvOM804Rqg12M12SPwJnnVdGVFTcvhPtbM_Vyde_STCsSaVyLTrYzFygyBcuhOXKuKvT-D045Cnqm2p1qbnKDD4yzxn3vnB10IgopBjwBRe3TYJWwpX6ekxxkItilkxV3RdcE9HT1eLxdZ-ZWgSNOWnZR7cCbQEkOlHkB83WNMVqHaeqch6DwYqIVJT5jxYK-MWwX97Y1di6MP74T4fphmBEqrDs-n372wX9Bb1-h5a3R9Znzqe0gxB5wAzx_mjY_cTtbiUl5SZafnLwKlIM4eX28RmvF7fBDBkQmmMr3hT0WTNRxvuIplf67sKg0M0S6AAAAATUG0NIA")
STRING3 = getenv("STRING_SESSION3", None)
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
    "https://telegra.ph/file/56d1760224589ee370186.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

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
