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
    
    def __init__(self, book_name="Name", book_author="Author", reading_date="0",\
                 book_rathing="0", url_fantlab="fantlab.ru"
                 ):
        self.book_name = book_name
        self.book_author = book_author
        self.reading_date = reading_date
        self.book_rathing = book_rathing
        self.url_fantlab = url_fantlab
    
    def book_add(self, file_name, index):
        pass
    
    def book_find(self):
        pass
    
    def book_return(self):
        pass
    

class File:
    "Text file class"
    
    def __init__(self, file_name="Defaut", input_text=""):
        self.file_name = file_name
        self.input_text = input_text
        
    def file_write(self):
        with open(self.file_name, 'a') as f:
            f.write(self.input_text)
            
    
    def file_read(self):
       file_r = open(self.file_name, 'r')
       return file_r
    
    def file_backup(self, file_name):
        pass
    

class Bot:
    """ Bot class"""

    def __init__(self, bot=bot, message=[], output="Default"):
        self.bot = bot
        self.message = message
        self.output = output
        
    def data_in(self, message, output):
        self.bot.reply_to(message, output)


    def data_out(self):
        pass
    
    
class Scrapper:
    """Scrapping and parsing html pages"""
    
    def __init__(self, key_word='', url='https://fantlab.ru/searchmain?searchstr='):
        self.key_word = key_word
        self.url = url
    
    def scrapping(self, url='https://fantlab.ru/searchmain?searchstr=', key_word=''):
        request = req.get(url + key_word)
        return request

    
    def parcing(self, request, message):
        soup = BeautifulSoup(request.text, 'html.parser')
        result = soup.find_all(class_='search-block works')
        if result == []:
            bot.reply_to(message, 'Ничего не найдено')
        else:
            for element in result:
                title = element.find_all(class_='title')
                if len(title) > 3:
                    number_elements = 3
                else:
                    number_elements = len(title)
                for i in title:
                    t = str(i.find('a'))
                    t = "fantlab.ru" + t[t.find('/'):t.rfind('"')]
                    bot.reply_to(message, t)
                    number_elements -= 1
                    if number_elements == 0:
                        break

        
    

@bot.message_handler(func=lambda message: True)  
def main(message):
    """main function"""
    
    output = "Привет, я бот_коллекционер. Храню список прочитанных вами книг.\
Но пока я ничего не умею"
    main_bot = Bot()
    main_bot.data_in(message, output)
    file_name = str(message.from_user.id)
    input_text = datetime.utcfromtimestamp(message.date + 10800).strftime('%Y-%m-%d %H:%M:%S ')\
                 + "Input message: " + message.text + "\n"
    text_log = File(file_name, input_text)
    text_log.file_write()
    scrapp = Scrapper()
    request = scrapp.scrapping(key_word=message.text)
    scrapp.parcing(request, message)
    
    

bot.polling(none_stop=True, interval=1)
