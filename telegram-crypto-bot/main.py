# Crypto Telegram bot developed by github.com/hotheahdhacker (Salman Qureshi)
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config #For token use here your own token
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import random
import mongodb
from datetime import datetime
import os
# import pandas as pd
# import lxml

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# port if deploying on heroku
#PORT = int(os.environ.get('PORT', '8443'))
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    user= update.message.from_user
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    mydict = {"username": user.username, "fname": user.first_name, "lname": user.last_name,"is_bot": user.is_bot, "id": user.id, "date": dt}

    try:
        x = mongodb.mycol.insert_one(mydict)
    except:
        print("Duplicate User")
        update.message.reply_text("Welcome Back!")
    update.message.reply_text('Hi! Thanks for choosing this bot! This bot is in alpha stage and lots of cool features will be added with time! \n /start - To Start \n /status - To Get Overall Crypto Market Status of Last 24hrs\n/winners - All Crypto coins/tokens that showed growth in last 24hrs\n/losers - All Crypto coins/tokens that showed loss in last 24hrs \n/help - For More info \n\n🧑Bot Developed by: @salmanually')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/status - To Get Overall Crypto Market Status of Last 24hrs \n/winners - All Crypto coins/tokens that showed growth in last 24hrs\n/losers - All Crypto coins/tokens that showed loss in last 24hrs\nThis Bot is in Alpha Version, with more features help page will be maintained!')

def status(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Request Processing... Plz Wait...")
    rand = random.random() #To overide cache
    URL = 'https://www.coinbase.com/price/s/top-gainers?v=' + str(rand)
    req = Request(URL , headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')

    results = soup.find(class_="MarketHealth__Value-sc-1a64a42-3")
    
    # return("🚀 The Market is Up 24% From Last 24 hrs 📈")
    update.message.reply_text(results.text)

def winners(update, context):
    update.message.reply_text("🚀📈 Winner coins/tokens in last 24 hrs... Fetching Plz Wait...")

    URL = 'https://coincodex.com/gainers-losers/'
    req = Request(URL , headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find_all('table', attrs={'class':'coins'})
    # table_body = table.find('tbody')
    data = table[0].find_all('tr')
    i = 0
    msg=""
    for el in data:
        cols = el.find_all('td')
        
        
        msg += "▶️"
        for td in cols:
           
            msg +=  td.text + "   "
        msg += "\n"
    update.message.reply_text(msg)

def losers(update, context):
    update.message.reply_text("🔻📉 Loser coins/tokens in last 24 hrs... Fetching Plz Wait...")

    URL = 'https://coincodex.com/gainers-losers/'
    req = Request(URL , headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find_all('table', attrs={'class':'coins'})
    # table_body = table.find('tbody')
    data = table[1].find_all('tr')
    i = 0
    msg=""
    for el in data:
        cols = el.find_all('td')
        
        
        msg += "▶️"
        for td in cols:
           
            msg +=  td.text + "   "
        msg += "\n"
    update.message.reply_text(msg)

    


# def echo(update, context):
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(config.token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("winners", winners))
    dp.add_handler(CommandHandler("losers", losers))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()