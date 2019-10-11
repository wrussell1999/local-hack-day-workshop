# Instructions

1. Create the following files:
    - `__main__.py`
    - `__init__.py`

2. Create a file for our code called `bot.py`
3. Add a `main()` function to `bot.py`
4. Go back to `__main__.py`
```python
from . import bot

if __name__ == '__main__':
    bot.main()
```
_this means the bot will be triggered with `python -m discord_bot`. The `main()` function will be the first thing to run.

5. Setup `config.json` and `discord_bot/config.py` file

```json
{
    "discord_token": "paste token here",
    "reddit_client_id": "paste id here",
    "reddit_client_secret": "paste secret here",
    "reddit_user_agent": "paste user agent here"
}
```

```python
import json

with open('config.json') as file:
    creds = json.load(file)
```

6. Add the imports to `bot.py`.

```python
import discord
from discord.ext import commands
from . import config
```


7. Create a `bot` object.

```python
bot = commands.Bot(command_prefix='?')
```

8. Add the code to get the bot to run

```python
 bot.run(config.creds['discord_token'])
```

9. Add an `on_ready()` function.

```python
@bot.event
async def on_ready():
    print('Ready!')
```

10. Test the code!

_You should see "Ready!" appear in your terminal._

11. Add command function

```python
@bot.command(description="Post a picture from a subreddit. Add deepfry as a 2nd argument for a filter.")
async def picture(ctx):
    args = ctx.message.clean_content.split(' ')
    theme = args[1]
    image = reddit.get_subreddit_image(theme)
    ctx.send(file=discord.File(image, 'image.png'))
```

12. Now we need to add the reddit code

_Create a new file in `discord_bot` called `reddit.py`._

```python
import praw
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
```

_Remember to add the imports to `bot.py`_

```python
from . import reddit
```

13. Deepfry time

_Make a file called `deepfry` inside `discord_bot`.

```python
from PIL import Image, ImageOps, ImageEnhance

def deepfry(image):
    image = Image.open(image)
    image = image.convert('RGB')
    width, height = image.width, image.height
    image = image.resize((int(width ** .75), int(height ** .75)), resample=Image.LANCZOS)
    image = image.resize((int(width ** .88), int(height ** .88)), resample=Image.BILINEAR)
    image = image.resize((int(width ** .9), int(height ** .9)), resample=Image.BICUBIC)
    image = image.resize((width, height), resample=Image.BICUBIC)
    image = ImageOps.posterize(image, 4)

    r = image.split()[0]
    r = ImageEnhance.Contrast(r).enhance(5.0)
    r = ImageEnhance.Brightness(r).enhance(1.5)
    r = ImageOps.colorize(r, (255, 0 , 0), (255, 255, 0))
    image = Image.blend(image, r, 0.75)
    image = ImageEnhance.Sharpness(image).enhance(0.0)
    
    image.save("deepfry.png")
```

_Inside `bot.py`, add the import `from . import deepfry` and ammend your `picture` command.

```python
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
```

14. Now go and add your own commands to your new bot!