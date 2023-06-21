import telebot
from telebot import types
from bs4 import BeautifulSoup
import random 
import requests
import os

bot_token = "6253446849:AAE3SdrY8OTRq7bC_vi07xoQCRdIqH73Hek"
bot = telebot.TeleBot(bot_token)
def get_game_help():
    response = requests.get('https://wargm.ru/games/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    game = random.choice(html.find_all(class_='cl-8 trim fw-b'))
    return(game.text)

@bot.message_handler(commands=['gamehelp'])
def messagge_processing(message):
    bot.send_message(message.chat.id, get_game_help())
bot.polling(non_stop=True)
