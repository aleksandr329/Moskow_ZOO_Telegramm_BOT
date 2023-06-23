import time
import telebot
from db import db_table_val, db_comment_save
from telebot import types
from logics import *
from parametrs import YOU_TOKEN
from text_check import text_check01


bot = telebot.TeleBot(YOU_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    us = message.from_user.id
    name = message.from_user.first_name
    fam = message.from_user.last_name
    nik = message.from_user.username
    db_table_val(us, name, fam, nik)  #<--Function to write the user to the database

    photo_start = open('photo/cat_start.jpg', 'rb')
    bot.send_photo(message.chat.id, photo_start)

    text1 = f'''<b>{name}</b>, добро пожаловать, в бот Московского зоопарка! 
    Мы хотим предложить вам пройти наш увликательный тест, по итогу которого вы сможете узнать кто является вашим тотемным животным!'''

    bot.send_message(message.chat.id, text1, parse_mode = 'HTML')
    time.sleep(10)
    photo_start2 = open('photo/photo_start_2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo_start2)
    text2 = f'''Нам всем уже не терпится поскорей начать! Если вам тоже нажмите кнопку ПРОЙТИ ТЕСТ 👇'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('ПРОЙТИ ТЕСТ 🦁')
    markup.add(btn1)
    bot.send_message(message.chat.id, text2,  reply_markup=markup, parse_mode='HTML')

@bot.message_handler(commands=['comment'])
def comment(message):
    mess1 = bot.reply_to(message, 'Пожалуйста, оставьте ваш отзыв!')
    bot.register_next_step_handler(mess1, comment_action)

def comment_action(message):
    data_user = (f'ID нашего пользователя->:{message.from_user.id}, Имя нашего пользователя->:{message.from_user.first_name}, фамилия->:{message.from_user.last_name}, Ник нейм->:{message.from_user.username}')
    db_comment_save(message.from_user.id, message.text)#<--Function that writes a comment to the database.
    c = [276606987, 5851216128]#<--Here you can write a list of ID of administrators who will receive mailings with new comments.
    for i in c:#<--This is the distribution function.
        bot.send_message(i, f'У нас новый отзыв, нам написал: <b>{data_user}</b>, и вот что он пишет: <b>{message.text}</b>', parse_mode='HTML')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn999 = types.KeyboardButton('Начать все сначала 🔄')
    markup.add(btn999)
    text1 = ('Спасибо вам большое, ваш отзыв поможет нам стать лучше!')
    bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


@bot.message_handler()
def programm(message):
    logics(message) #<--Function for main logic

    if text_check01(message.text): #<--Checking if the user enters some unscripted text
        text1 = ('''<b>К сожаление наш БОТ 🤖 не понимает что вы написали😕 нажмите команду 👉🏻 /start 👈🏻 чтобы пройти тест</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')



if __name__ == "__main__":

    bot.polling(none_stop=True)


