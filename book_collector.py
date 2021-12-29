import telebot
import requests as req
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
from datetime import datetime
from telegram_token import token

bot = telebot.TeleBot(token)


class Book:
    """Create Book class"""
    
    def __init__(self, name, author, date, rathing, url):
        self.name = 'Name'
        self.author = 'Author'
        self.date = '0'
        self.rathing = '0'
        self.url = 'fantlab.ru'
    
    def book_add(self, file_name, index):
        pass
    
    def book_find(self):
        pass
    
    def book_return(self):
        pass
    

class Files:
    "Text file class"
    
    def __init__(self, file_name):
        file_name = "Default"
        
    def file_write(self, file_name):
        pass
    
    def file_read(self, file_name):
        pass
    
    def file_backup(self, file_name):
        pass
    

class Bot:
    """ Bot class"""

    def __init__(self, bot=bot, message=[], output="Default"):
        self.bot = bot
        self.message = message
        self.output = "Default"
        
    def data_in(self, message, output):
        self.bot.reply_to(message, output)


    def data_out(self):
        pass
    
    
class Scrapper:
    """Scrapping and parsing html pages"""
    
    def __init__(self, key_word, url):
        pass
    
    def scrapping(self, key_word):
        pass
    
    def parcing(self, text):
        pass
    

@bot.message_handler(func=lambda message: True)  
def main(message):
    """main function"""
    output = "Привет, я бот_коллекционер. Храню список прочитанных вами книг.\
Но пока я ничего не умею"

    main_bot = Bot()
    main_bot.data_in(message, output)

bot.polling(none_stop=True, interval=1)