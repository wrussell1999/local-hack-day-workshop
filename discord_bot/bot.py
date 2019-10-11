import discord
from discord.ext import commands
from . import config
from . import deepfry
from . import reddit

bot = commands.Bot(command_prefix='?')

def main():
    bot.run(config.creds['discord_token'])

@bot.event
async def on_ready():
    print('Ready!')

@bot.command(description="Post a picture from a subreddit, Add deepfry as a 2nd argument for a filter.")
async def picture(ctx):
    args = ctx.message.clean_content.split(' ') 
    theme = args[1]
    image = reddit.get_subreddit_image(theme)
        
    if len(args) >= 3 and args[2] == 'deepfry':
        deepfry.deepfry(image)
        await ctx.send(file=discord.File('deepfry.png'))
    else:
        await ctx.send(file=discord.File(image, 'image.png'))
