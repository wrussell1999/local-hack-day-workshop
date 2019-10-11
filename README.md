
![(https://localhackday.mlh.io/learn/locations/1859)](/images/lhd_logo.png)
# Reddit Meme    Discord Bot Workshop
[Local Hack Day - Learn](https://localhackday.mlh.io/learn/locations/1859) workshop at the University of Birmingham run by Will Russell.

The presentation can be found [here](https://docs.google.com/presentation/d/1Dpa35En2z70bxEA0AQd0QHqfcTFVvOtqDp2O27mCJeo/edit?usp=sharing).

The following libraries were used:
- [discord.py](https://discordpy.readthedocs.io/en/latest/)
- [PRAW](https://praw.readthedocs.io/en/latest/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [requests](https://realpython.com/python-requests/)

## Setup

You'll need some tokens/unique IDs/secrets to get started. Follow the guides below to get these. These will all belong inside of `config.json`. See `template/config_template.json` for a template.

- Get Setup with the [Discord API here](discord.md)

- Get Setup with the [Reddit API here](reddit.md)

## Development

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Run

```bash
(.venv) $ python -m discord_bot
```

## Credit

The deepfry functionality was used from [deeppyer](https://github.com/Ovyerus/deeppyer). Some adjustments were made for maximum edge.
