from dotenv import load_dotenv
import diseasy
from diseasy import require_env
from diseasy.errors import EnvVariableMissing
import os

load_dotenv()

try:
    TOKEN = require_env("BOT_TOKEN")
except EnvVariableMissing as e:
    print(f"Required option not found: {e}")
    exit(1)

PREFIX = os.getenv("PREFIX", "!")
intents = ["guilds", "messages"]

bot = diseasy.Bot(intents=intents, prefix=PREFIX)

# Cogs
cogs = [
    "cogs.utils",
    "cogs.moderation",
    "cogs.reward",
    "cogs.integration",
    "cogs.games",
]

for cog in cogs:
    bot.load_extension(cog)

@bot.event(name="on_ready")
async def on_ready(*args):
    print("<bot.name> is Online.")

bot.run(TOKEN)