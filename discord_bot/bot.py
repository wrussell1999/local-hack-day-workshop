import discord
from discord.ext import commands
import praw
import requests
import random
from io import BytesIO
from . import config

bot = commands.Bot(command_prefix='?')
reddit = praw.Reddit(client_id=config.creds['reddit_client_id'],
                     client_secret=config.creds['reddit_client_secret'],
                     user_agent=config.creds['reddit_user_agent'])

def main():
    bot.run(config.creds['discord_token'])

def get_subreddit_image(name):
    subreddit = reddit.subreddit(name)
    urls = []
    for submission in reddit.subreddit(name).hot(limit=25):
        if submission.domain == 'i.redd.it':
            urls.append(submission.url)
    
    response = requests.get(random.choice(urls))
    image = BytesIO(response.content)
    return image

@bot.event
async def on_ready():
    print('Ready!')

@bot.command(description="Post a picture from a subreddit")
async def picture(ctx):
    theme = ctx.message.clean_content.split(' ')[1]
    image = get_subreddit_image(theme)
    await ctx.send(file=discord.File(image, 'image.png'))
