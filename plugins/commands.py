from config import Config

def startText(update,context):
 update.message.reply_text(Config.START_TEXT)

def helpText(update,context):
 update.message.reply_text(Config.HELP_TEXT)