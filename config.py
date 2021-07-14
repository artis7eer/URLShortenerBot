import os

def get_env(var):
  return os.environ.get(var,None)

class Config:
  BOT_TOKEN = get_env('BOT_TOKEN')
  
  START_TEXT = 'Hi, I am alive'
  
  HELP_TEXT = 'Send me a url to get shortened link'
  
  