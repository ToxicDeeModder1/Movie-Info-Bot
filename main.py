# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram import Client

bot_token = os.environ["1953666437:AAE5HWyC1CWJ3W1NocApiL4ZwbXKZG1HGj8"]
api_id = int(os.environ["8522555"])
api_hash = os.environ["9e0b9e90b854c23fe89ee57b0a75ff32"]

plugins = dict(
    root="plugins"
)

Bot = Client(
    "Movie-Info-Bot",
    bot_token=1953666437:AAE5HWyC1CWJ3W1NocApiL4ZwbXKZG1HGj8,
    api_id=8522555,
    api_hash=9e0b9e90b854c23fe89ee57b0a75ff32,
    plugins=plugins
)

Bot.run()
