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

from config import Config
from telegram.constants import ParseMode
async def startText(update,context):
 await update.message.reply_text(Config.START_TEXT)

async def helpText(update,context):
 await update.message.reply_text(Config.HELP_TEXT,parse_mode = ParseMode.MARKDOWN,disable_web_page_preview=True)
 
async def aboutText(update,context):
 await update.message.reply_text(Config.ABOUT_TEXT,parse_mode = ParseMode.MARKDOWN,disable_web_page_preview=True)