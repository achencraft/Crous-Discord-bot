import os
import discord
import structlog
from dotenv import load_dotenv
from os.path import join, dirname
from discord.ext import commands


log = structlog.get_logger()
dotenv_path = join(dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    log.info('loading environment')
    load_dotenv(dotenv_path)


TOKEN = os.getenv('BOT_TOKEN')
BOT_PREFIX = os.getenv('BOT_PREFIX', '/ ')
BOT_NAME = os.getenv('BOT_NAME','BOT-CROUS')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=BOT_PREFIX,  case_insensitive=True, intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    action = discord.Game("🍟 /menu")
    await bot.change_presence(status=discord.Status.online, activity=action)


bot.run(TOKEN, bot=True, reconnect=True)
