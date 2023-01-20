# URLShortenerBot - A Telegram Bot To short long urls
# Copyright (C) 2023 by Abdul Razaq <https://github.com/Artis7eeR>
# URLShortenerBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# URLShortenerBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from telegram.ext import (
    filters, 
    MessageHandler,
    CommandHandler, 
    CallbackQueryHandler,
    ApplicationBuilder,
)
from config import Config
from plugins.commands import *
from plugins.shortener import *
import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    bot = ApplicationBuilder().token(Config.BOT_TOKEN).build()

    bot.add_handler(MessageHandler(
        filters.Regex(pattern=Config.URL_PATTERN), URIShortener))
    bot.add_handler(CallbackQueryHandler(cbackResponse))
    bot.add_handler(CommandHandler('start', startText))
    bot.add_handler(CommandHandler('help', helpText))
    bot.add_handler(CommandHandler('about', aboutText))

    # start the bot
    bot.run_polling()


if __name__ == '__main__':
    main()
