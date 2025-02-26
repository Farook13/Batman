import re
from os import environ, getenv
from Script import script

# Pattern for validating IDs
id_pattern = re.compile(r'^.\d+$')

# Helper function to parse boolean-like environment variables
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot Core Settings
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '12618934'))
API_HASH = environ.get('API_HASH', '49aacd0bc2f8924add29fb02e20c8a16')
BOT_TOKEN = environ.get('BOT_TOKEN', '7857321740:AAHSUfjwO3w6Uffmxm9vCUMl36FtXl5-r6w')

# Admin and Channel Settings
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5032034594').split()]
USERNAME = environ.get('COLONEL', "https://t.me/")  # Admin username or link
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002467149516'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/batmanmoviehub')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002256041072').split()]

# Database Settings
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://saidalimuhamed88:iladias2025@cluster0.qt4dv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'My_Tg_files')

# Additional Channel Settings
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '1002467149516'))  # Log channel for API-related info
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS', '0'))  # Channel where uploaded movies are deleted from bot
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '0'))  # Verification log channel
auth_channel = environ.get('AUTH_CHANNEL', 'https://t.me/zoromovie13')  # Force-sub channel
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002187734788'))  # Support group ID
request_channel = environ.get('REQUEST_CHANNEL', 'https://t.me/request_channel77')  # Request channel for user requests
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '0'))  # Channel for movie updates
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/zoromovie13')  # Support chat link

# Verification Settings (without premium-related verification)
IS_VERIFY = is_enabled('IS_VERIFY', False)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/zoromovie13")  # How-to-use tutorial link

# File Filtering Options
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip", "web-dl", "bluray", "hdr", "fhd", "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2025, 2002, -1)]
SEASONS = [f'season {i}' for i in range(1, 23)]

# Convert channel links to IDs if applicable
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# Bot Appearance Settings
START_IMG = (environ.get('START_IMG', 'https://graph.org/file/8ac9be0d690c03e4a6d58-052f8fcda4d18922b8.jpg https://envs.sh/t7j.jpg https://envs.sh/t7c.jpg  https://envs.sh/t7G.jpg https://envs.sh/t7L.jpg https://envs.sh/t7c.jpg https://envs.sh/t7_.jpg https://envs.sh/tzT.jpg ')).split()  # Start command image
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://envs.sh/eWS.jpg')  # Force-sub image
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]  # Reaction emojis

# Bot Behavior Settings
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))  # Auto-delete timer for files
AUTO_FILTER = is_enabled('AUTO_FILTER', True)  # Enable auto-filter
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)  # Allow search in PM
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', False)  # Send movie updates (off by default)
PORT = environ.get('PORT', '5000')  # Port for hosting
MAX_BTN = int(environ.get('MAX_BTN', '8'))  # Max buttons in inline keyboard
AUTO_DELETE = is_enabled('AUTO_DELETE', True)  # Auto-delete messages
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))  # Time before auto-delete
IMDB = is_enabled('IMDB', True)  # Enable IMDB info  # Default file caption
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')  # IMDB description template
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', True)  # Detailed IMDB descriptions
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)  # Protect forwarded files
SPELL_CHECK = is_enabled('SPELL_CHECK', True)  # Enable spell check for searches
LINK_MODE = is_enabled('LINK_MODE', True)  # Enable link generation for files

# Stream and Hosting Settings
STREAM_MODE = bool(environ.get('STREAM_MODE', True))  # Enable streaming
MULTI_CLIENT = False  # Multi-client support (off by default)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))  # Sleep threshold for requests
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # Ping interval (20 minutes)
ON_HEROKU = 'DYNO' in environ  # Detect if running on Heroku
URL = environ.get("FQDN", "")  # Custom URL for hosting

# Bot Settings Dictionary
SETTINGS = {
    'spell_check': SPELL_CHECK,
    'auto_filter': AUTO_FILTER,
    'file_secure': PROTECT_CONTENT,
    'auto_delete': AUTO_DELETE,
    'template': IMDB_TEMPLATE,
    'tutorial': TUTORIAL,
    'log': LOG_VR_CHANNEL,
    'imdb': IMDB,
    'link': LINK_MODE,
    'is_verify': IS_VERIFY
}

# Admin Commands (stripped of premium-related commands)
admin_cmds = [
    "/refresh", "/index", "/send", "/leave",
    "/ban", "/unban", "/broadcast", "/grp_broadcast",
    "/delreq", "/channel", "/del_file", "/delete",
    "/deletefiles", "/deleteall",
    "All These Commands Can Be Used Only By Admins.",
    "⚡ powered by @COLONEL BOTS"
]

# User Commands (stripped of premium/referral-related commands)
cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"}
]