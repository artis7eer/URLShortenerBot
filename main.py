from telegram.ext import Filters,MessageHandler,CommandHandler,Updater,CallbackQueryHandler
from config import Config
from plugins.commands import (
  startText,
  helpText
  )
from plugins.shortener import *


def main():
 updater = Updater(Config.BOT_TOKEN,use_context=True)

 dp = updater.dispatcher
 
 #url regex
 dp.add_handler(MessageHandler(Filters.regex(pattern=".*http*."),uri_shortener))
 
 
 #callback
 dp.add_handler(CallbackQueryHandler(shorten_cback))
 

 #commands
 dp.add_handler(CommandHandler('start',startText))
 dp.add_handler(CommandHandler('help',helpText))
 
 #start the bot
 updater.start_polling()
 updater.idle()

if __name__=='__main__':
    main()