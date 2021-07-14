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


from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import pyshorteners

shorten = pyshorteners.Shortener()

def tiny_short(uri):
 tiny_url=shorten.tinyurl.short(uri)
 return tiny_url

def chilp_short(uri):
 chilp_url=shorten.chilpit.short(uri)
 return chilp_url

def clck_short(uri):
 clck_url=shorten.clckru.short(uri)
 return clck_url

def dagd_short(uri):
 dagd_url=shorten.dagd.short(uri)
 return dagd_url

def isgd_short(uri):
 isgd_url=shorten.isgd.short(uri)
 return isgd_url

def osdb_short(uri):
 osdb_url=shorten.osdb.short(uri)
 return osdb_url

def qps_short(uri):
 qps_url=shorten.qpsru.short(uri)
 return qps_url



def uri_shortener(update,context):
  keyboard = [
  [
  InlineKeyboardButton("TinyUrl.com", callback_data="tiny"),
  InlineKeyboardButton("Chilp.it", callback_data=f"chilp")
  ],
  [
  InlineKeyboardButton("Clck.ru", callback_data="clck"),
  InlineKeyboardButton("Da.gd", callback_data="dagd")
  ],
  [
  InlineKeyboardButton("Is.gd", callback_data="isgd"),
  InlineKeyboardButton("Os.db", callback_data="osdb")],
  [InlineKeyboardButton("Qps.ru", callback_data="qps")]
  ]

  ikeyboard = InlineKeyboardMarkup(keyboard)
  update.message.reply_text("""Choose The Service:""",reply_markup=ikeyboard,reply_to_message_id=update.message.message_id)

def shorten_cback(update,context):
  query = update.callback_query
  if update.callback_query.message.reply_to_message is not None:
   uri=update.callback_query.message.reply_to_message.text
   cbdata=query.data
  try:
    if cbdata.startswith("tiny"):
      sh_uri=tiny_short(uri)
      query.edit_message_text(sh_uri)
    elif cbdata.startswith("chilp"):
      sh_uri=chilp_short(uri)
      query.edit_message_text(sh_uri)
    elif cbdata.startswith("clck"):
      sh_uri=clck_short(uri)
      query.edit_message_text(sh_uri)
    elif cbdata.startswith("dagd"):
      sh_uri=dagd_short(uri)
      query.edit_message_text(sh_uri)
    elif cbdata.startswith("isgd"):
      sh_uri=isgd_short(uri)
      query.edit_message_text(sh_uri)
    elif cbdata.startswith("osdb"):
      sh_uri=osdb_short(uri)
      query.edit_message_text(sh_uri)
    elif cbdata.startswith("qps"):
      sh_uri=qps_short(uri)
      query.edit_message_text(sh_uri)
  except Exception as e:
    query.edit_message_text(str(e))