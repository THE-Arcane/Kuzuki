#Copyright (C) 2021 Free Software @d3nvil @FakeMasked , Inc.[ https://t.me/d3nvil https://t.me/FakeMasked ]
#Everyone is permitted to copy and distribute verbatim copies
#of this license document, but changing it is not allowed.
#The GNGeneral Public License is a free, copyleft license for
#software and other kinds of works.
#PTB13 Updated by @noobanon

# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = ""
    OWNER_ID = "5330301316"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "II_ZEUS_XD_II"
    TOKEN = '5381445827:AAEy8d8Q4CMwZRzzj0yLT8Dom5zD3u8aoCk'

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://xpaenmuc:BM__fqKXtkkrx0FkdgQWXMzrfR0UwiU4@castor.db.elephantsql.com/xpaenmuc'  # needed for any database modules
    MESSAGE_DUMP = '' # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation']
    WEBHOOK = False
    DONATION_LINK = ''
    URL = ""

    # OPTIONAL
    SUDO_USERS = [0]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [0]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [0]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5432
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = ''  # banhammer marie sticker
    STRICT_GBAN = True
    STRICT_GMUTE = True
    CUSTOM_CMD = True  # Allow ! commands as well as /
    API_OPENWEATHER = '' # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
