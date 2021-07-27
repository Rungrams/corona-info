# Author: Fayas (https://github.com/rungrams) (@rungrams)

import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "Corona-Info-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://api.sumanjay.cf/covid/?country="

START_TEXT = """
Hello {}, I am a simple corona information of a country telegram bot.

Made by @rungram
"""

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⭕ SUPPORT ⭕', url='https://telegram.me/rungram')
        ]]
    )

@rungrams.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@rungrams.on_message(filters.private & filters.text)
async def reply_info(bot, update):
    country = update.text.replace(" ", "+").lower()
    reply_markup = BUTTONS
    await update.reply_text(
        text=covid_info(country),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )

async def covid_info(country_name):
    try:
        r = requests.get(API + country_name)
        info = r.json()
        country = info['country']
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""
--**Covid 19 Information**--

Country : `{country}`
Actived : `{active}`
Confirmed : `{confirmed}`
Deaths : `{deaths}`
ID : `{info_id}`
Last Update : `{last_update}`
Latitude : `{latitude}`
Longitude : `{longitude}`
Recovered : `{recovered}`

Made by @rungram
"""
        return covid_info
    except Exception as error:
        return error

Rungrams.run()
