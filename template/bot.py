import discord
from discord.ext import commands
from . import config

bot = commands.Bot(command_prefix='?')

def main():
     bot.run(config.creds['discord_token'])

@bot.event
async def on_ready():
    print('Ready!')
