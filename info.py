import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value is None:
        return default
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', 29155314))  # Use default if environment variable not set
API_HASH = environ.get('API_HASH', '8c612d2371bb07cd405adec606582b60')  # Use default if environment variable not set
BOT_TOKEN = environ.get('BOT_TOKEN', '8016251564:AAH_HUZaeyVhGE0GSX1xQfkBp7W3U9-qdmg')  # Add your bot token dynamically or hardcode it

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://graph.org/file/494ea30f3523c2c40203d-fdc3c6120a737ae59e.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6424894431').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002005654267').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', 0)) if environ.get('AUTH_CHANNEL') else None
AUTH_GROUPS = [int(ch) for ch in environ.get('AUTH_GROUP', '').split()] if environ.get('AUTH_GROUP') else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', '')
DATABASE_NAME = environ.get('DATABASE_NAME', "yuvrajvs")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'MOVIESPRIMEHUB1')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1002394165174))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MOVIESPRIMEHUB1')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b>\n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled. Bot will be showing IMDB details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found. Users will be redirected to send /start to Bot PM instead of sending files directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled; files will be sent in PM instead of requiring /start.\n")
LOG_STR += ("SINGLE_BUTTON is Found. Filename and file size will be shown in a single button instead of two separate buttons.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled; filename and file size will be shown as different buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value '{CUSTOM_FILE_CAPTION}'. Your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION found. Default captions of the file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled. Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode is enabled. The bot will suggest related movies if the movie is not found.\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode is disabled.\n")
LOG_STR += (f"MAX_LIST_ELM found. Long lists will be shortened to the first {MAX_LIST_ELM} elements.\n" if MAX_LIST_ELM else "Full list of casts and crew will be shown in the IMDB template. Restrict them by adding a value to MAX_LIST_ELM.\n")
LOG_STR += f"Your current IMDB template is:\n{IMDB_TEMPLATE}"
