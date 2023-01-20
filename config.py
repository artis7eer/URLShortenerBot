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

from dotenv import load_dotenv
import os

load_dotenv()


class Config:
  BOT_TOKEN = os.getenv('BOT_TOKEN')
  
  START_TEXT = """Hi,This is link URL shortener bot.
Send me a link🔗 to get the Shorted URL.
Use /help to get help
  """
  HELP_TEXT = """
  Available commands 
  /start - Check if bot is active
  /help - Get this message
  /about - Get Info about Bot
  
  """
  ABOUT_TEXT = """
[Source Code](https://github.com/Artis7eeR/URLShortenerBot)❤
Version : 0.1✨
Created By [Abdul Razaq](https://github.com/artis7eer) 👨‍💻
Powered By [Cyphers](https://t.me/cyphersofficial) ✔
If any queries Ask me via [Telegram](https://t.me/artis7eer)
©2023 
  """
  
  # regex pattern from : https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url
  URL_PATTERN = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
  