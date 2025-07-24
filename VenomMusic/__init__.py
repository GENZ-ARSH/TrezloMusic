from VenomMusic.core.bot import Venom
from VenomMusic.core.dir import dirr
from VenomMusic.core.git import git
from VenomMusic.core.userbot import Userbot
from VenomMusic.misc import dbb, heroku

from .logging import LOGGER

LOGGER(__name__).info("🔥 Starting TrezloMusicBot initialization...")

# Safe startup modules
try:
    dirr()
    LOGGER(__name__).info("✅ dirr() initialized")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ dirr() failed: {e}")

try:
    git()
    LOGGER(__name__).info("✅ git() executed")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ git() failed: {e}")

try:
    dbb()
    LOGGER(__name__).info("✅ dbb() initialized")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ dbb() failed: {e}")

try:
    heroku()
    LOGGER(__name__).info("✅ heroku() initialized")
except Exception as e:
    LOGGER(__name__).warning(f"⚠️ heroku() failed: {e}")


# Core bots
try:
    app = Venom()
    LOGGER(__name__).info("✅ Venom bot initialized")
except Exception as e:
    LOGGER(__name__).error(f"❌ Venom init failed: {e}")

try:
    userbot = Userbot()
    LOGGER(__name__).info("✅ Userbot initialized")
except Exception as e:
    LOGGER(__name__).error(f"❌ Userbot init failed: {e}")


# Platform APIs
from .platforms import *

try:
    Apple = AppleAPI()
    Carbon = CarbonAPI()
    SoundCloud = SoundAPI()
    Spotify = SpotifyAPI()
    Resso = RessoAPI()
    Telegram = TeleAPI()
    YouTube = YouTubeAPI()
    LOGGER(__name__).info("✅ All platform APIs initialized")
except Exception as e:
    LOGGER(__name__).error(f"❌ Platform API init failed: {e}")
