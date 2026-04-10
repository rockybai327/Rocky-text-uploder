import os

API_ID = API_ID = 22492036

API_HASH = os.environ.get("API_HASH", "b4d672fb51ddf8abaa62c6db1f756bab")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8617813128:AAGKzIJttATtjy_oBXEIujqu6OZxreNN0oU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 8617813128))

LOG = -1001952769436

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "8617813128").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


