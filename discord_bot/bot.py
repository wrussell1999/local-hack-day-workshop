import discord
from discord.ext import commands
import praw
import requests
import random
from io import BytesIO
from PIL import Image, ImageOps, ImageEnhance
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

def deepfry(image):
    image = Image.open(image)
    image = image.convert('RGB')
    width, height = image.width, image.height
    image = image.resize((int(width ** .75), int(height ** .75)), resample=Image.LANCZOS)
    image = image.resize((int(width ** .88), int(height ** .88)), resample=Image.BILINEAR)
    image = image.resize((int(width ** .9), int(height ** .9)), resample=Image.BICUBIC)
    image = image.resize((width, height), resample=Image.BICUBIC)
    image = ImageOps.posterize(image, 4)
    print("ENHANCE")
    r = image.split()[0]
    r = ImageEnhance.Contrast(r).enhance(2.0)
    r = ImageEnhance.Brightness(r).enhance(1.5)
    r = ImageOps.colorize(r, (254, 0 , 2), (255, 255, 15))
    print("BLEND")
    image = Image.blend(image, r, 0.75)
    image = ImageEnhance.Sharpness(image).enhance(200.0)
    print("SHARPEN")
    image.save("test.png")
    # work out how to return as file like obj
    print("SAVED")

@bot.event
async def on_ready():
    print('Ready!')

@bot.command(description="Post a picture from a subreddit")
async def picture(ctx):
    args = ctx.message.clean_content.split(' ') 
    theme = args[1]
        
    image = get_subreddit_image(theme)
    await ctx.send(file=discord.File(image, 'image.png'))
    if len(args) == 3 and args[2] == 'deepfry':
        deepfry(image)
        await ctx.send(file=discord.File('test.png'))
        
