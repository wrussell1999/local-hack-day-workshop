import praw
from discord.ext.commands.errors import CommandInvokeError
from discord.ext import commands
import requests
from io import BytesIO
from . import config

def get_subreddit_image(name):

    reddit = praw.Reddit(client_id=config.creds['reddit_client_id'],
                     client_secret=config.creds['reddit_client_secret'],
                     user_agent=config.creds['reddit_user_agent'])

    subreddit = reddit.subreddit(name)
    url = ""

    while url == "":
        for submission in reddit.subreddit(name).new(limit=1):
            if submission.domain == 'i.redd.it':
                url = submission.url

    response = requests.get(url)
    image = BytesIO(response.content)
    return image
