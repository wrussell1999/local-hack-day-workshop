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
_this means the bot will be triggered with `python -m discord_bot`. The `main()` function will be the first thing to run._