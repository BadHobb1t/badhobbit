import telebot
from telebot import types
from bs4 import BeautifulSoup
import random 
import requests
import os

bot_token = "6253446849:AAE3SdrY8OTRq7bC_vi07xoQCRdIqH73Hek"
bot = telebot.TeleBot(bot_token)

def get_intresting_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    return(fact.text)

def get_game_help():
    response = requests.get('https://wargm.ru/games/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    game = random.choice(html.find_all(class_='cl-8 trim fw-b'))
    return(game.text)

#def get_game_help_with_gerne():
#    response = requests.get('https://wargm.ru/games/')
#    x=input()
#    response = response.content
#    game = 'https://wargm.ru/games/???'.replace("???",x)
#    return(game.text)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    bot.send_message(message.chat.id, "Здарова!", reply_markup=keyboard)

@bot.message_handler(commands=['fact'])
def message_processing(message):
    bot.send_message(message.chat.id, get_intresting_fact())
6
@bot.message_handler(commands=['gamehelp'])
def messagge_processing(message):
    bot.send_message(message.chat.id, get_game_help())

#@bot.message_handler(commands=['gamehelpwj'])
#def messagge_processing(message):
#    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
#    bot.send_message(message.chat.id, "Введите жанр на англ.языке", reply_markup=keyboard)
#    bot.send_message(message.chat.id, get_game_help_with_gerne())
bot.polling(non_stop=True)
