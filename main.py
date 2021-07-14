# URLShortenerBot - A Telegram Bot To short long urls
#Copyright (C) 2021 by Rasak <https://github.com/Artis7eeR>
#URLShortenerBot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#URLShortenerBot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.



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