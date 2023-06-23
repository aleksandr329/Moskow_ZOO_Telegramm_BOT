import time
from telebot import types
import telebot
from main import *

#This file describes all the main logic for executing commands.

def logics(message):
    if message.text == 'ПРОЙТИ ТЕСТ 🦁':
        text1 = ('''<b>Какую природную среду вы предпочитаете?</b>''')
        photo2 = open('photo/zemlya_vs_voda.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('Земля 🌏')
        btn3 = types.KeyboardButton('Вода 🌊')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn2, btn3, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Начать все сначала 🔄':
        start(message)

    if message.text == 'Оставить коментарий 💭':
        bot.send_message(message.chat.id, f'Чтобы оставить коментарий нажмите сюда 👉🏻 /comment 👈🏻')


    if message.text == 'Земля 🌏':
        text1 = ('''<b>Что вам нравится кушать?</b>''')
        photo2 = open('photo/food.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn4 = types.KeyboardButton('Овощи 🍆🥔🥕')
        btn5 = types.KeyboardButton('Мясо 🍖')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn4, btn5, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Мясо 🍖':
        video1 = open('video/video_myso.MP4', 'rb')
        bot.send_video(message.chat.id, video1)
        time.sleep(4)
        text1 = ('''<b>Что вам нравится в животных?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn6 = types.KeyboardButton('Мудрость 👨🏻‍🎓👩🏼‍🎓')
        btn7 = types.KeyboardButton('Быстрота 🏃🏻‍♂️🏃🏻‍♀️')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn6, btn7, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Мудрость 👨🏻‍🎓👩🏼‍🎓':
        photo1 = open('photo/nice.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Какой звук вас успокаивает?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn8 = types.KeyboardButton('Шелест листьев 🍂')
        btn9 = types.KeyboardButton('Шум волн 🌊')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn8, btn9, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Быстрота 🏃🏻‍♂️🏃🏻‍♀️':
        photo1 = open('photo/4_seasons.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Какое время года вам нравится больше всего?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn10 = types.KeyboardButton('Зима ❄⛄')
        btn11 = types.KeyboardButton('Осень 🍁')
        btn12 = types.KeyboardButton('Лето ☀')
        btn13 = types.KeyboardButton('Весна 🌷')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn10, btn11, btn12, btn13,btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Зима ❄⛄':
        photo1 = open('photo/loneliness.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Вы предпочитаете жить?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn14 = types.KeyboardButton('В одиночистве 👤')
        btn15 = types.KeyboardButton('В коллективе 👥')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn14, btn15, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Осень 🍁':
        photo1 = open('photo/loneliness.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Вы предпочитаете жить?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn14 = types.KeyboardButton('В одиночистве 👤')
        btn15 = types.KeyboardButton('В коллективе 👥')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn14, btn15, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Лето ☀':
        photo1 = open('photo/scales.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Что важнее в жизни?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn16 = types.KeyboardButton('Денежный достаток 💰')
        btn17 = types.KeyboardButton('Семья 👪')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn16, btn17, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Весна 🌷':
        photo1 = open('photo/scales.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Что важнее в жизни?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn16 = types.KeyboardButton('Денежный достаток 💰')
        btn17 = types.KeyboardButton('Семья 👪')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn16, btn17, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Семья 👪':
        video1 = open('video/famyly.mp4', 'rb')
        bot.send_video(message.chat.id, video1)
        text1 = ('''<b>Какой вкус вы любите больше всего?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn18 = types.KeyboardButton('Соленый 🍚')
        btn19 = types.KeyboardButton('Сладкий 🍰')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn18, btn19, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Денежный достаток 💰':
        photo1 = open('photo/skrudj.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Надеемся ваша любовь к деньгам не такая, как у старины Скруджа 🤑')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/reptar.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Любите кататься на электросамокатах?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn20 = types.KeyboardButton('Да конечно 🛴')
        btn21 = types.KeyboardButton('Нет вы что, это опасно 😱🤕')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn20, btn21, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'В одиночистве 👤':
        photo1 = open('photo/odinochestvo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Да, иногда нужно побыть на едине с самим собой 🙂')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/type_music.png', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Какой тип музыки вы предпочитаете?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn22 = types.KeyboardButton('Рок 🤘🏻')
        btn23 = types.KeyboardButton('Хип-Хоп 🤙🏻')
        btn24 = types.KeyboardButton('Классическую 🎻')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn22, btn23, btn24, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'В коллективе 👥':
        photo1 = open('photo/kollektiv.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Вместе веселей правда ведь 🕺👯🕺')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/time_sutki.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Какое время суток вам нравится больше?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn25 = types.KeyboardButton('День 🌞')
        btn26 = types.KeyboardButton('Ночь 🌑')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn25, btn26, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Ночь 🌑':
        photo1 = open('photo/no4ka.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Тогда эта картинка вам точно понравится ☝')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/socium.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Как вы общаетесть с новыми людьми?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn27 = types.KeyboardButton('Охотно и открыто 😀')
        btn28 = types.KeyboardButton('Осторожно и застенчиво 😑')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn27, btn28, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'День 🌞':
        photo1 = open('photo/le_soley.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Тогда эта картинка вам точно понравится ☝')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/ogon_voda.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Какой элемент природы вам нравится больше?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn29 = types.KeyboardButton('Огонь 🔥')
        btn30 = types.KeyboardButton('Вода 💦')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn29, btn30, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Рок 🤘🏻':
        photo1 = open('photo/gory_plag.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Где вам комфортнее?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn31 = types.KeyboardButton('Горы 🌄')
        btn32 = types.KeyboardButton('Пляж 🏖')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn31, btn32, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Хип-Хоп 🤙🏻':
        video1 = open('video/rap.MOV', 'rb')
        bot.send_video(message.chat.id, video1)
        time.sleep(4)
        text1 = ('''<b>Какой тип погоды вам нравится больше?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn33 = types.KeyboardButton('Жаркий и солнечный ☀😓')
        btn34 = types.KeyboardButton('Прохладный и дождливый ☔')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn33, btn34, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Классическую 🎻':
        photo1 = open('photo/classic.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        time.sleep(4)
        text1 = ('''<b>Какой тип погоды вам нравится больше?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn33 = types.KeyboardButton('Жаркий и солнечный ☀😓')
        btn34 = types.KeyboardButton('Прохладный и дождливый ☔')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn33, btn34, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Шелест листьев 🍂':
        photo1 = open('photo/4_seasons.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Какое время года вам нравится больше всего?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn10 = types.KeyboardButton('Зима ❄⛄')
        btn11 = types.KeyboardButton('Осень 🍁')
        btn12 = types.KeyboardButton('Лето ☀')
        btn13 = types.KeyboardButton('Весна 🌷')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn10, btn11, btn12, btn13, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Шум волн 🌊':
        video1 = open('video/volny.MOV', 'rb')
        bot.send_video(message.chat.id, video1)
        text1 = ('''<b>Что вы выберете, если предстоит выбирать между яблоком и бананом?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn35 = types.KeyboardButton('Яблоко 🍏')
        btn36 = types.KeyboardButton('Банан 🍌')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn35, btn36, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Яблоко 🍏':
        photo1 = open('photo/apple.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Да яблоки это действительно вкусно!')
        bot.send_message(message.chat.id, text1)
        time.sleep(4)
        text2 = ('''<b>Как вы проводите свое свободное время?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn37 = types.KeyboardButton('Активно с друзьями 🤾🏻‍♀️🤼‍♂️⛷⛹')
        btn38 = types.KeyboardButton('Спокойно в одиночестве 🍩🤫☕')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn37, btn38, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Активно с друзьями 🤾🏻‍♀️🤼‍♂️⛷⛹':
        photo1 = open('photo/otdyx.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Отдых это отдельный вид искусства!')
        bot.send_message(message.chat.id, text1)
        time.sleep(4)
        text2 = ('''<b>Какой цвет на машине смотрится лучше?</b>''')
        photo2 = open('photo/colors.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn39 = types.KeyboardButton('Желтый 💛')
        btn40 = types.KeyboardButton('Конечно розовый 🌸')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn39, btn40, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Хоккей 🏒':
        photo1 = open('photo/hokey_life.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        time.sleep(4)
        text1 = ('''<b>Какой цвет на машине смотрится лучше?</b>''')
        photo2 = open('photo/colors.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn39 = types.KeyboardButton('Желтый 💛')
        btn40 = types.KeyboardButton('Конечно розовый 🌸')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn39, btn40, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Овощи 🍆🥔🥕':
        photo1 = open('photo/vegan.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        time.sleep(4)
        text1 = ('''<b>Какая рабка вам нравится больше?</b>''')
        photo2 = open('photo/fisch.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn41 = types.KeyboardButton('Красная 🔴')
        btn42 = types.KeyboardButton('Синяя 🐟')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn41, btn42, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Красная 🔴':
        photo1 = open('photo/fisch_red.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Тогда эта картинка вам точно понравится! ☝')
        bot.send_message(message.chat.id, text1)
        time.sleep(4)
        text2 = ('''<b>Как бы вы описали свою личность?</b>''')
        photo2 = open('photo/lichnost.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn43 = types.KeyboardButton('Мягкая и добрая 🤗')
        btn44 = types.KeyboardButton('Сильная и энергичная 💪🏻')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn43, btn44, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Синяя 🐟':
        photo1 = open('photo/fisch_blu.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Тогда эта картинка вам точно понравится! ☝')
        bot.send_message(message.chat.id, text1)
        time.sleep(4)
        text2 = ('''<b>Как бы вы описали свою личность?</b>''')
        photo2 = open('photo/lichnost.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn43 = types.KeyboardButton('Мягкая и добрая 🤗')
        btn44 = types.KeyboardButton('Сильная и энергичная 💪🏻')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn43, btn44, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Мягкая и добрая 🤗':
        photo1 = open('photo/dobro.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Правильно нужно быть добрее! Эта конфетка для вас 🍬')
        bot.send_message(message.chat.id, text1)
        time.sleep(4)
        text2 = ('Ок едем дальше, нашему боту уже не терпится узнать результат вашего теста 🤖')
        bot.send_message(message.chat.id, text2)
        time.sleep(4)
        text3 = ('''<b>Вы любите путишевствовать?</b>''')
        photo2 = open('photo/putishevstvie.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn45 = types.KeyboardButton('Да это всегда весело ✈')
        btn46 = types.KeyboardButton('Нет это утомляет 🙅🏻‍♂️')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn45, btn46, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Банан 🍌':
        video1 = open('video/banana.MOV', 'rb')
        bot.send_video(message.chat.id, video1)
        time.sleep(4)
        text1 = ('''<b>Вы любите путишевствовать?</b>''')
        photo2 = open('photo/putishevstvie.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn45 = types.KeyboardButton('Да это всегда весело ✈')
        btn46 = types.KeyboardButton('Нет это утомляет 🙅🏻‍♂️')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn45, btn46, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Да это всегда весело ✈':
        photo1 = open('photo/ura_putichestvie.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Главное не забыть дома очки 😎')
        bot.send_message(message.chat.id, text1)
        time.sleep(4)
        text2 = ('''<b>Какая погода вам по душе?</b>''')
        photo2 = open('photo/dozd.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn47 = types.KeyboardButton('Солнечная 🌞')
        btn48 = types.KeyboardButton('Дождливая 🌧️')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn47, btn48, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')

    elif message.text == 'Футбол ⚽':
        photo1 = open('photo/futbol.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Животные тоже любят играть в футбол!')
        bot.send_message(message.chat.id, text1)
        time.sleep(4)
        'Футбол ⚽'
        text2 = ('''<b>Какая погода вам по душе?</b>''')
        photo2 = open('photo/dozd.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn47 = types.KeyboardButton('Солнечная 🌞')
        btn48 = types.KeyboardButton('Дождливая 🌧️')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn47, btn48, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Нет это утомляет 🙅🏻‍♂️':
        photo1 = open('photo/kto_ty.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Бывает такое 😸')
        bot.send_message(message.chat.id, text1)
        time.sleep(4)
        text2 = ('''<b>Вы предпочитаете быть один или с компанией?</b>''')
        photo2 = open('photo/grupa.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn49 = types.KeyboardButton('Одному лучше 🚶')
        btn50 = types.KeyboardButton('С компанией 🕺👯')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn49, btn50, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Сильная и энергичная 💪🏻':
        photo1 = open('photo/mamkin_ka4ok.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Да быть сильным здорово! Можно без проблем помогать тем кто послабее вас 😉')
        bot.send_message(message.chat.id, text1)
        time.sleep(4)
        text2 = ('''<b>Какой вид спорта вам нравится больше?</b>''')
        photo2 = open('photo/plavanie_vs_beg.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn51 = types.KeyboardButton('Плавание 🏊🏼‍♂️')
        btn52 = types.KeyboardButton('Бег 🏃🏻‍♂️')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn51, btn52, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Плавание 🏊🏼‍♂️':
        photo1 = open('photo/trener.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        time.sleep(4)
        text1 = ('''<b>Что вы любите делать в свободное время?</b>''')
        photo2 = open('photo/free_time.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn53 = types.KeyboardButton('Читать книги ️📖')
        btn54 = types.KeyboardButton('Смотреть фильмы 📺')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn53, btn54, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Слушать и наблюдать 🤫':
        text1 = ('''<b>Что вы любите делать в свободное время?</b>''')
        photo2 = open('photo/free_time.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn53 = types.KeyboardButton('Читать книги ️📖')
        btn54 = types.KeyboardButton('Смотреть фильмы 📺')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn53, btn54, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Бег 🏃🏻‍♂️':
        video1 = open('video/beg.mp4', 'rb')
        bot.send_video(message.chat.id, video1)
        text1 = ('''<b>Любите бег так же, как эти ребята?</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        text2 = ('''<b>Вам нравятся люди?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn55 = types.KeyboardButton('Веселые 🤣')
        btn56 = types.KeyboardButton('Умные 🧠')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn55, btn56, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Общатся 🗣':
        photo1 = open('photo/lui_defines.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Вам нравятся люди?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn55 = types.KeyboardButton('Веселые 🤣')
        btn56 = types.KeyboardButton('Умные 🧠')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn55, btn56, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Читать книги ️📖':
        video1 = open('video/4tenie.MOV', 'rb')
        bot.send_video(message.chat.id, video1)
        time.sleep(4)
        text1 = ('''<b>Что выберешь?</b>''')
        photo2 = open('photo/arbuz.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn57 = types.KeyboardButton('Мороженное 🍦')
        btn58 = types.KeyboardButton('Арбузик 🍉')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn57, btn58, btn999)
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Вода 🌊':
        photo1 = open('photo/riba_v_vode.png', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Наш БОТ 🤖 мечтает научится плавать!')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/priroda.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Вы часто бываете на природе?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn59 = types.KeyboardButton('Да ⛺')
        btn60 = types.KeyboardButton('Нет, очень редко 🏠')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn59, btn60, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Да ⛺':
        photo1 = open('photo/les_eda.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Главное правило в лесу! Не брать чужую еду!')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/les_derevia.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Что на ваш взглад нужнее в лесу?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn59 = types.KeyboardButton('Фонарик 🔦')
        btn60 = types.KeyboardButton('Дрова ✔')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn59, btn60, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Нет, очень редко 🏠':
        photo1 = open('photo/gribi.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Жаль, там очень здорово!')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/lui_defines.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Как вы обычно выглядите?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn59 = types.KeyboardButton('Серьезно и задумчиво 🤨')
        btn60 = types.KeyboardButton('Легко и задорно 😀')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn59, btn60, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Серьезно и задумчиво 🤨':
        photo1 = open('photo/abisin.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Ого надеемся не на столько серьезно!')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/music_kot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Какой тип музыки вы предпочитаете?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn61 = types.KeyboardButton('Классика 🎷')
        btn62 = types.KeyboardButton('Поп-Музыка 💃')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn61, btn62, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Классика 🎷':
        photo1 = open('photo/kompachka.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>Когда вы в компании что вам больше нравится делать?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn63 = types.KeyboardButton('Общатся 🗣')
        btn64 = types.KeyboardButton('Слушать и наблюдать 🤫')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn63, btn64, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Поп-Музыка 💃':
        photo1 = open('photo/opiat2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Как думаете называется эта картина?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn65 = types.KeyboardButton('Кто нибудь выгуляйте собаку 🐕')
        btn66 = types.KeyboardButton('Опять двойка 2️⃣')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn65, btn66, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Опять двойка 2️⃣':
        photo1 = open('photo/nu_konechno.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        time.sleep(4)
        photo2 = open('photo/futbol_vs_hokey.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text1 = ('''<b>Какой вид спорта вам нравится?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn67 = types.KeyboardButton('Футбол ⚽')
        btn68 = types.KeyboardButton('Хоккей 🏒')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn67, btn68, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Кто нибудь выгуляйте собаку 🐕':
        photo1 = open('photo/nooooooo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>К сожалению это не правильный ответ 🙁</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/futbol_vs_hokey.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Какой вид спорта вам нравится?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn67 = types.KeyboardButton('Футбол ⚽')
        btn68 = types.KeyboardButton('Хоккей 🏒')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn67, btn68, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Легко и задорно 😀':
        photo1 = open('photo/zima_vs_leto.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>В какое время года вы бы поехали в отпуск?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn69 = types.KeyboardButton('Летом ☀')
        btn70 = types.KeyboardButton('Зимой ☃')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn69, btn70, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Дрова ✔':
        photo1 = open('photo/polet.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Как думаете называется эта картина?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn71 = types.KeyboardButton('Наконец лето 🐷')
        btn72 = types.KeyboardButton('Вперед в мечте 🐖')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn71, btn72, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Вперед в мечте 🐖':
        photo1 = open('photo/nu_konechno.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Часто любите бегать, прыгать?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn73 = types.KeyboardButton('Да не могу остановится 🤸🏼‍♂️')
        btn74 = types.KeyboardButton('Лучше поделать что то еще 🎮')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn73, btn74, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Наконец лето 🐷':
        photo1 = open('photo/sogelenie.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        time.sleep(4)
        text1 = ('''<b>Часто любите бегать, прыгать?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn73 = types.KeyboardButton('Да не могу остановится 🤸🏼‍♂')
        btn74 = types.KeyboardButton('Лучше поделать что то еще 🎮')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn73, btn74, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Фонарик 🔦':
        photo1 = open('photo/fonarik.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Да с ним будет немного веселее 👍🏻! Главное взять побольше батареек 🔋')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/salvador.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Как думаете какой породы был домашний питомец Сальвадора Дали?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn75 = types.KeyboardButton('Оцелот 😺')
        btn76 = types.KeyboardButton('Гепард 🐆')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn75, btn76, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Оцелот 😺':
        photo1 = open('photo/ocelot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('И это правильный ответ!')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/perecus.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Вы любите перекус на ходу, или лучше потерпеть и дома спокойно покушать?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn77 = types.KeyboardButton('Мне нравится есть на лету 🦅')
        btn78 = types.KeyboardButton('Лучше спокойно дома 🍕')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn77, btn78, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Летом ☀':
        photo1 = open('photo/perecus.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('''<b>Вы любите перекус на ходу, или лучше потерпеть и дома спокойно покушать?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn77 = types.KeyboardButton('Мне нравится есть на лету 🦅')
        btn78 = types.KeyboardButton('Лучше спокойно дома 🍕')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn77, btn78, btn999)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Зимой ☃':
        photo1 = open('photo/zimny_otdyx.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Да главное не простудится 🤒')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/pitomec.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>У вас есть домашний питомец?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn79 = types.KeyboardButton('Да я очень его люблю 🐶')
        btn80 = types.KeyboardButton('Нет это много проблем ⛔')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn79, btn80, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Гепард 🐆':
        photo1 = open('photo/nooooooo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('К сожаление это неправильны ответ! 🤖')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/nevispalsa.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Вы рано ложитесь спать?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn81 = types.KeyboardButton('Да стараюсь жить по режиму 🛌🏻')
        btn82 = types.KeyboardButton('Все ни как не получится  🤦🏻')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn81, btn82, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Да я очень его люблю 🐶':
        photo1 = open('photo/dog_kot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Здорово наш БОТ 🤖 тоже любит домашних питомцев!')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/nevispalsa.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Вы рано ложитесь спать?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn81 = types.KeyboardButton('Да стараюсь жить по режиму 🛌🏻')
        btn82 = types.KeyboardButton('Все ни как не получится  🤦🏻')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn81, btn82, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Нет это много проблем ⛔':
        photo1 = open('photo/dog_kot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text1 = ('Будем надеятся, со временем вы поменяете свой взгляд!')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(4)
        photo2 = open('photo/nevispalsa.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        text2 = ('''<b>Вы рано ложитесь спать?</b>''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn81 = types.KeyboardButton('Да стараюсь жить по режиму 🛌🏻')
        btn82 = types.KeyboardButton('Все ни как не получится  🤦🏻')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn81, btn82, btn999)
        bot.send_message(message.chat.id, text2, reply_markup=markup, parse_mode='HTML')


## results## results## results## results## results## results## results## results## results## results## results## results## results## results## results## results## results
##⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇


    if message.text == 'Да конечно 🛴':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/kamych_kot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы КАМЫШОВЫЙ КОТ! Мы если честно сразу это подозревали 🙃</b>''')
        text3 = ('''
    Интересный факт о КАМЫШОВЫХ КОШКАХ:
    Коты активно пользуются норами - в них пережидают непогоду, дневной зной, прячутся от опасности. Однако 
    самостоятельно норы не роют, предпочитают пользоваться брошенными барсучьими и лисьими. Подолгу в одной и той же 
    норе не живут, меняя убежища в целях безопасности. Камышовые коты, в отличие от домашней кошки, не только не боятся 
    воды, но и любят купаться, даже погружаясь в воду с головой. Одна из гипотез, объясняющая мотивы такого поведения - 
    уничтожение запаха хищника, поскольку он отпугивает добычу во время охоты.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Желтый 💛':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/kamych_kot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы КАМЫШОВЫЙ КОТ! Мы если честно сразу это подозревали 🙃</b>''')
        text3 = ('''
    Интересный факт о КАМЫШОВЫХ КОШКАХ:
    Коты активно пользуются норами - в них пережидают непогоду, дневной зной, прячутся от опасности. Однако 
    самостоятельно норы не роют, предпочитают пользоваться брошенными барсучьими и лисьими. Подолгу в одной и той же 
    норе не живут, меняя убежища в целях безопасности. Камышовые коты, в отличие от домашней кошки, не только не боятся 
    воды, но и любят купаться, даже погружаясь в воду с головой. Одна из гипотез, объясняющая мотивы такого поведения - 
    уничтожение запаха хищника, поскольку он отпугивает добычу во время охоты.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Нет вы что, это опасно 😱🤕':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_belka.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы КАПСКАЯ ЗЕМЛЯНАЯ БЕЛКА! Это не большой но очень отважный зверек 🐿</b>''')
        text3 = ('''
    Интересный факт о КАПСКИХ ЗЕМЛЯНЫХ БЕЛКАХ:
    Обычно зверьки активны в течение дня, ночь проводят в норах. От дневной жары также часто спасаются под землёй. Есть 
    у них и своеобразный зонтик от солнца - пушистый хвост. Кроме того, такая гигиеническая процедура, как купание в 
    песке, по-видимому, также хорошо охлаждает. Земляные белки хорошие землекопы, и их нора может располагаться на 
    площади до 700 кв. метров. В ней множество ходов, камер и отнорков. В такой норе может быть до 100 входов-выходов. 
    Белки часто используют одну нору совместно с сурикатами или желтыми мангустами, причем отношения с сурикатами у них 
    равноправные, а с мангустами носят симбиотический характер.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Конечно розовый 🌸':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_belka.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы КАПСКАЯ ЗЕМЛЯНАЯ БЕЛКА! Это не большой но очень отважный зверек 🐿</b>''')
        text3 = ('''
    Интересный факт о КАПСКИХ ЗЕМЛЯНЫХ БЕЛКАХ:
    Обычно зверьки активны в течение дня, ночь проводят в норах. От дневной жары также часто спасаются под землёй. Есть 
    у них и своеобразный зонтик от солнца - пушистый хвост. Кроме того, такая гигиеническая процедура, как купание в 
    песке, по-видимому, также хорошо охлаждает. Земляные белки хорошие землекопы, и их нора может располагаться на 
    площади до 700 кв. метров. В ней множество ходов, камер и отнорков. В такой норе может быть до 100 входов-выходов. 
    Белки часто используют одну нору совместно с сурикатами или желтыми мангустами, причем отношения с сурикатами у них 
    равноправные, а с мангустами носят симбиотический характер.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Соленый 🍚':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
    ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_trubkozub.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ТРУБКОЗУБ! Ого наш БОТ 🤖 тоже всегда мечтал быть ТРУБКОЗУБОМ 🐽</b>''')
        text3 = ('''
    Интересный факт о ТРУБКОЗУБАХ:
    Трубкозуб – обладатель крепких когтей и прекрасный землекоп, поэтому древнеегипетский бог пустыни и разрушения Сет 
    иногда изображался с головой этого животного. Однако это не мешало и не мешает людям на него иногда охотиться, 
    поскольку мясо по вкусу напоминает свинину. Коренные африканцы из кожи животного делают кожаные браслеты, а белые 
    колонисты во времена освоения Африки делали из кожи трубкозубов ремни и сбрую. Из зубов трубкозуба изготавливают 
    ожерелья, якобы охраняющие от болезней и приносящие удачу. У местных жителей существует также поверье, что при сборе
    крылатых особей термитов для еды «урожай» будет лучше, если в корзину положить когти трубкозуба.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Сладкий 🍰':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
    ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_mangust.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ПОЛОСАТЫЙ МАНГУСТ! Ого наш БОТ 🤖 тоже всегда мечтал быть ПОЛОСАТЫМ МАНГУСТОМ</b>''')
        text3 = ('''
    Интересный факт о ПОЛОСАТЫХ МАНГУСТАХ:
    Полосатые мангусты – дневные зверьки. Они просыпаются рано утром и с заходом солнца прячутся в убежище. Ночью из 
    укрытий они не показываются. «Домами» обычно служат термитники и расщелины скал. Нор, подобно сурикатам, они не 
    роют, но могут обустроить небольшую брошенную нору. Известно, что убежища мангусты меняют раз в два-три дня. 
    Исключения наблюдаются лишь в том случае, если в группе есть маленькие детёныши. Полосатые мангусты живут довольно 
    большими группами, число зверьков в группе от 7 до 40, в среднем 15-20. Участок обитания группы составляет около 
    2 кв. км, на занимаемой площади полосатые мангусты могут использовать до 40 различных укрытий. Ночью зверьки спят в 
    одном «доме», согревая друг друга, утром выходят на кормёжку. Если в группе есть малыши, то они остаются в укрытии. 
    Вместе с детьми постоянно находится кто-то из сородичей, чаще это взрослые самцы. Няньки» сменяют друг друга, чтобы 
    поесть. Месячные детёныши уже выходят на охоту вместе со взрослыми особями.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Осторожно и застенчиво 😑':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
    ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_sich.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы МОХНОНОГИЙ СЫЧ! Это небольших размеров сова, но от этого она не менее красива 🦉</b>''')
        text3 = ('''
    Интересный факт о МОХНОНОГИХ СЫЧАХ:
    Мохноногий сыч – исключительно ночная птица. Охотится из засады и, возможно, более других сов ориентируется по слуху.

Ведет осёдлый образ жизни, однако в некоторых районах наблюдаются осенне-зимние кочевки, связанные, вероятно, с изменением кормовых условий.

Полёт бесшумный, порхающий (как у бабочки). Избегает открытых мест, так как там он становится заметным для более крупных хищников.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    elif message.text == 'Спокойно в одиночестве 🍩🤫☕':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
    ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_sich.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = (
            '''<b>И вот какой результат теста: Вы МОХНОНОГИЙ СЫЧ! Это небольших размеров сова, но от этого она не менее красива 🦉</b>''')
        text3 = ('''
    Интересный факт о МОХНОНОГИХ СЫЧАХ:
    Мохноногий сыч – исключительно ночная птица. Охотится из засады и, возможно, более других сов ориентируется по слуху.
    Ведет осёдлый образ жизни, однако в некоторых районах наблюдаются осенне-зимние кочевки, связанные, вероятно, с 
    изменением кормовых условий. Полёт бесшумный, порхающий (как у бабочки). Избегает открытых мест, так как там он 
    становится заметным для более крупных хищников.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Охотно и открыто 😀':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_kunnica.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы КАМЕННАЯ КУНИЦА! Класс, очень жизнерадостное животное 🐾</b>''')
        text3 = ('''
    Интересный факт о КАМЕННЫХ КУНИЦАХ:
    Каменная куница активна главным образом  в ночное время, а днем она прячется в укрытии. Естественными укрытиями 
    ей служат расщелины скал, груды камней, норы других животных; дупла она занимает очень редко. Поселившись рядом 
    с человеком, каменная куница выбирает чердаки, подвалы и тому подобные укрытия. Свой дом она выстилает перьями, 
    травой, кусочками шерсти, а рядом с человеком – тряпочками, бумагой. Охотится каменная куница чаще всего на 
    земле, по деревьям она вообще лазает редко. Зимой при высоком снеговом покрове куницы передвигаются по тропам, 
    проложенным другими животными (например, зайцами) или человеком (лыжня). Каменная куница ведет одиночный образ 
    жизни и  вне сезона размножения достаточно агрессивна по отношению к пришельцам - сородичам обоего пола. Свою 
    территорию куницы метят особым пахучим секретом, выделяемом анальными железами. Площадь индивидуального участка
        колеблется от 12 до 200 га, причем у самцов она больше, чем у самок, и зимой меньше, чем весной и летом.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Огонь 🔥':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_secretarjpg.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ПТИЦА-СЕКРЕТАРЬ! Класс, отважная и смелая птица 🐔</b>''')
        text3 = ('''
    Интересный факт о ПТИЦАХ-СЕКРЕТАРЯХ:
    Птица-секретарь, в отличие от большинства хищных птиц, почти все время проводит на земле, проходя в день в поисках 
    пищи по 20-30 км. Для того чтобы взлететь, секретарю требуется значительный разбег. Однако во время брачного периода
    и гнездования, самец периодически парит над гнездом, защищая его от возможных врагов. Вне периода гнездования 
    секретари ведут кочевой образ жизни, при этом пара, которая образуется на всю жизнь, держится вместе, не выпуская 
    друг друга из поля зрения. Гнездовой участок фиксируется и охраняется птицами только на период гнездования. Ночуют 
    птицы-секретари на деревьях.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Вода 💦':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_slon_4erepaha.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы СЛОНОВАЯ ЧЕРЕПАШКА! Круто, на секунду эти ребята живут болше 100 лет 😉</b>''')
        text3 = ('''
    Интересный факт о СЛОНОВЫХ ЧЕРЕПАХАХ:
    Слоновые черепахи ведут дневной образ жизни, хотя могут быть активны и в ночное время. В условиях тропического 
    климата активны круглый год. Слоновые черепахи являются одними из самых долгоживущих животных. В природе они 
    доживают до 100 лет, в неволе – до 150 и даже больше. Пьют слоновые черепахи редко, вполне довольствуясь росой и 
    соком растений; без воды они могут обходиться до 6 месяцев.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Горы 🌄':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_iguana.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ИГУАНА! Круто, наш БОТ 🤖 точно видит ваши сходства!</b>''')
        text3 = ('''
    Интересный факт о ИГУАНАХ:
    Большую часть жизни зеленые игуаны проводят на деревьях, причем активны они только в дневное время суток. Прохладные
    ночи рептилии сидят на толстых ветках в среднем и нижнем ярусе леса, а с восходом солнца стараются забраться 
    повыше, где подолгу греются, замерев на ветке. Солнечные лучи повышают температуру тела, а под действием
    ультрафиолетового излучения вырабатывается витамин D, способствующий пищеварению. Лишь хорошо согревшись в течение
    нескольких часов, игуаны начинают активно кормиться. В ненастную или прохладную погоду игуаны держатся на земле,
    сохраняя внутреннее тепло. В случае падения с дерева даже с 10-15 метровой высоты  (что случается довольно редко)
    игуаны не разбиваются. Падая, они стараются зацепиться когтями задних конечностей за листву. Врагов в природе у 
    игуан много: хищные птицы и млекопитающие, крокодилы, крупные змеи. Однако в реальности взрослые крупные  особи 
    успешно избегают опасности. Спасению от врагов способствует покровительственная окраска ящериц и их защитное 
    поведение. При опасности чаще всего игуана спасается бегством или, бросившись в воду, быстро уплывает. При активной
    защите ящерица раздувает горловой мешок и все тело, шипит и делает головой выпады в сторону противника. Если такие
    угрозы не помогают, игуаны могут больно кусаться или сильно бить хвостом.  ''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Пляж 🏖':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_kayman.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ЧЕРНЫЙ КАЙМАН! Круто, наш БОТ 🤖 точно видит ваши сходства!</b>''')
        text3 = ('''
    Интересный факт о ЧЕРНЫХ КАЙМАНАХ:
    Черные кайманы довольно агрессивные животные, но, по мнению ряда специалистов, они редко вступают в прямые 
    территориальные конфликты друг с другом.  Ведут одиночный образ жизни; только в период засухи они собираются вместе 
    в непересыхающих водоемах. Охотятся черные кайманы ночью, чему способствует их черная кожа. Днем, для поддержания 
    температуры тела  (230) крокодилы часто греются на солнце, лежа либо в воде на мелководье, либо на берегу. Черная 
    кожа в данном случае способствует лучшему поглощению солнечной энергии. Враги в природе есть только у молодых, 
    некрупных черных кайманов: это и хищные рыбы, и другие крокодилы, и анаконды, и хищные птицы, и ягуары. Когда же 
    кайманы достигают примерно 1 м в длину, естественных врагов у них практически не остается.  ''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Жаркий и солнечный ☀😓':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_tamarin.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы КРАСНОРУКИЙ ТАМАРИН! Не думайте что это какая то простая обезьянка 🐒 она такая же крутая как и вы!</b>''')
        text3 = ('''
    Интересный факт о КРАСНОРУКИХ ТАМАРИНАХ:
    У краснорукого тамарина большие, почти безволосые уши и лицо. Окраска головы и туловища однотонная – темно-
    коричневая или чёрная. Характерным признаком, по которому можно безошибочно узнать краснорукого тамарина – 
    красновато-желтые лапы – и передние, и задние. Анатомическое строение всего рода тамаринов отличается от строения 
    более крупных обезьян Нового Света. На всех пальцах, кроме большого, у них имеются видоизмененные когти вместо 
    ногтей, кроме того - два коренных зуба (вместо трех) в каждой челюсти. Как и у других игрунковых, резцы нижней 
    челюсти у тамаринов наклонены вперёд, позволяя зверькам делать надрезы на коре деревьев для добывания сока. 
    Обезьянки активны в дневное время, держатся в кронах деревьев. Когда ловят наземную добычу, могут прыгать на землю.
    Ночью спят в дуплах деревьев и развилках ветвей. Во время отдыха на ветках сидят, обвив себя длиннющим хвостом и
    прижавшись боками друг к другу.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Прохладный и дождливый ☔':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_udav.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы УДАВ! Вы не такой простой человек каким показались нашему БОТУ 🤖 на первый взгляд!</b>''')
        text3 = ('''
    Интересный факт об УДАВАХ:
    Обыкновенный удав ведет как наземный, так и древесный образ жизни, прекрасно лазает по вертикальным поверхностям, 
    что позволяет ему добывать пищу не только на земле. Однако по деревьям лазают молодые, более легкие змеи, с 
    возрастом и увеличением веса, они чаще охотятся на земле. Обычно удавы встречаются неподалеку от рек и ручьев и 
    великолепно плавают. Нередко они занимают норы средних по размеру млекопитающих, где прячутся от потенциальных 
    врагов. Активны в сумерках и ночью, но могут днем греться на солнце, когда ночные температуры слишком низкие. 
    Обыкновенные удавы довольно спокойные, флегматичные животные. По наблюдениям специалистов особи из Центральной 
    Америки более раздражительны, громко шипят и совершают угрожающие броски при беспокойстве. Особи из Южной Америки 
    более спокойны и легче приручаются. Во время линьки удавы становятся более агрессивными и осторожными, поскольку 
    помутнение глаз усложняет им ориентацию в пространстве. Вне брачного периода ведут одиночный образ жизни. 
    Питание и кормовое поведение
    Добычу обыкновенного удава составляют млекопитающие, птицы, иногда другие рептилии. Охотятся эти удавы из засады, 
    лежа в укрытии и подстерегая жертву. Но могут быть и активными охотниками, особенно в местах с недостаточным 
    количеством подходящей добычи. Активная охота чаще наблюдается в ночное время. Умерщвляет жертву удав, сдавливая ее 
    кольцами своего мощного тела. При этом жертва погибает не от удушья, как полагали раньше, а от непоступления крови в
    сердце и мозг. Зубы удава помогают проталкивать добычу в глотку, а мускулы тела – дальше в желудок. 
    Полное переваривание добычи в зависимости от ее размера и окружающей температуры происходит в течение 4-6 дней.
    После этого змея может не есть от недели до нескольких месяцев в связи с низким уровнем метаболизма.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Солнечная 🌞':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_pavlin.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ПАВЛИН! Красивый правда ведь 😍</b>''')
        text3 = ('''
    Интересный факт о ПАВЛИНАХ:
    Павлины обычно держатся небольшими группами, где на одного самца приходится 4-5 самок. Павлины очень осторожны и 
    своими громкими криками предупреждают других животных об опасности. Сами же они при опасности стараются убежать, не 
    прибегая к полету. Несмотря на свой длинный «хвост» бегают они быстро и лавируют в зарослях очень ловко. Летать 
    павлины могут, но не высоко и не долго. Однако ночуют и отдыхают павлины на деревьях, забираясь довольно высоко. 
    Каждый вечер они возвращаются на ночевку на одно и то же дерево, предварительно посетив место водопоя. Устраиваясь 
    на ночлег, павлины обычно громко кричат. Утро также начинается с водопоя, после чего павлины отправляются на поиски
    пищи. Во внегнездовое время павлины часто «пасутся» стайками в 40-50 птиц. Осенью, после завершения сезона 
    размножения, павлины линяют, и самцы полностью теряют свой шлейф. Врагов у павлинов много, это и крупные хищные
    млекопитающие, например, леопарды, и хищные птицы, причем как дневные, так и ночные, так что осторожность павлинам
    необходима.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Дождливая 🌧️':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_kuskus.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы КАРЛИКОВЫЙ ЛЕТУЧИЙ КУСКУС! Он такой крошечный, но очень храбрый зверек 🐭</b>''')
        text3 = ('''
    Интересный факт о КАРЛИКОВЫХ ЛЕТУЧИХ КУСКУСАХ:
    Карликовые летучие кускусы — ловкие и очень подвижные зверки — активны обычно ночью, а в пасмурную погоду — и днём. 
    В темную фазу суток их поведение характеризуется всплесками активности (кормление, передвижение), сменяющимися более
    спокойными периодами, когда зверьки чистятся, просто сидят на месте, или уходят в гнездо. Об их поведении в природе
    известно немного. Основные данные получены из наблюдений в зоопарках. По-видимому, у этих зверьков нет четких границ
    территории, но есть свои тропы, которые они регулярно метят. Животных встречали в группах до 20 особей, но 
    неизвестно, постоянны ли они. Особи из соседних групп относятся друг к другу доброжелательно. На теле кускусов есть 
    8 различных запаховых желез. О точных функциях секреции известно очень мало, но они наверняка играют роль в личном
    распознавании зверьков и при спаривании. Кускусы строят шарообразные гнёзда из разнообразного растительного 
    материала. Их гнёзда находили в разнообразных местах — от дупел деревьев и брошенных птичьих гнёзд до телефонных 
    будок. В одном гнезде, как правило, отдыхает сразу несколько животных — и самцы, и самки.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Одному лучше 🚶':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_pingi.png', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ПАПУАНСКИЙ ПИНГВИНЧИК! Очень красивый ПАПУАНСКИЙ ПИНГВИНЧИК 🐧</b>''')
        text3 = ('''
    Интересный факт о ПАПУАНСКИХ ПИНГВИНАХ:
    Живут папуанские пингвины колониями, насчитывающими несколько сотен пар. Их поведение в колонии вполне соответствует
    поведению всех колониальных птиц с взаимовыручкой и столкновениями внутри колонии. При этом каждая пара имеет свой 
    гнездовой участок, который она ревностно охраняет. Колонии каждый год перемещаются на несколько метров, но  иногда 
    по непонятным причинам могут сместиться на много километров. Обычно колонии находятся в 1-2 км от моря. Под водой 
    папуанские пингвины достигают скорости 36 км/час, что делает их самыми быстрыми из всех пингвинов. Погружаться они 
    могут на глубину до 200 м и находиться под водой до 7 минут. В поисках пищи эти птицы могут проплывать в день до 26 
    км. После завершения сезона размножения взрослые папуанские пингвины проводят некоторое время в море, накапливая 
    жировой запас перед линькой. Линька продолжается 2-3 недели, и все это время птицы остаются на берегу и не кормятся.
    У взрослых папуанских пингвинов на суше врагов нет, а в море на них охотятся морские львы, морские леопарды и 
    касатки. В колониях пингвинов нередко хищничают поморники и каракары.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'С компанией 🕺👯':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_black_lebed.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ЧЕРНЫЙ ЛЕБЕДЬ! Невероятной красоты 😍🤪</b>''')
        text3 = ('''
    Интересный факт о ЧЕРНЫХ ЛЕБЕДЯХ:
    До заселения европейцами Австралии считалось, что лебеди имеют только белое оперение, но открытие в 1697 году 
    экспедицией под руководством Виллема Вламинка на западе континента огромной популяции черных лебедей изменило это 
    представление. Правда, до сих пор можно услышать старейшее крылатое выражение древнеримского поэта Ювенала — 
    «хороший человек так же редок, как черный лебедь». В Европе долгие годы из-за траурного оперения черный лебедь был 
    пугающей птицей и считался вестником беды . Но с середины XIX века эту необычную птицу стали активно завозить в 
    Европу и Северную Америку для украшения парков и водоемов. На родине в Австралии вид подвергся активному истреблению.
    Во время линьки лебедь (как и другие гусеобразные) на некоторое время теряет способность летать и становится легкой
    добычей. Численность лебедей быстро сократилась.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Веселые 🤣':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_martischka_diana.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы МАРТЫШКА ДИАНА! Невероятной красоты 😍🤪</b>''')
        text3 = ('''
    Интересный факт о МАРТЫШКАХ ДИАНА:
    Дневные обезьяны, ночью спят высоко на деревьях. Эти обезьяны живут небольшими группами с одним взрослым самцом и 
    несколькими самками. Основной единицей сообщества является семья, состоящая из родственников по материнской линии.
    Связь мать — дочь обычно продолжается всю жизнь, а сыновья по достижении половой зрелости покидают родную семью и 
    присоединяются к другой группе или на какое-то время становятся одиночками. Взрослые самки, члены одной семейной 
    группы, часто занимаются грумингом (расчесывание и очистка шерсти друг у друга), или сидят, просто прижавшись друг к
    другу, или объединяются, чтобы отразить чье-то нападение. Детеныши объединяются со своими старшими сестрами. 
    Интересно, что маленький детеныш имеет в группе более высокий статус, чем его старшие сестры. Подросшие самцы, как 
    только покидают материнскую группу, теряют свой унаследованный статус, но они могут присоединиться к группе своих 
    старших братьев.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Умные 🧠':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_stepnoy_kot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы СТЕПНОЙ КОТ! Какой красавчик! Правда ведь?</b>''')
        text3 = ('''
    Интересный факт о СТЕПНЫХ КОТАХ:
    Дневные обезьяны, ночью спят высоко на деревьях. Эти обезьяны живут небольшими группами с одним взрослым самцом и 
    несколькими самками. Основной единицей сообщества является семья, состоящая из родственников по материнской линии.
    Связь мать — дочь обычно продолжается всю жизнь, а сыновья по достижении половой зрелости покидают родную семью и 
    присоединяются к другой группе или на какое-то время становятся одиночками. Взрослые самки, члены одной семейной 
    группы, часто занимаются грумингом (расчесывание и очистка шерсти друг у друга), или сидят, просто прижавшись друг к
    другу, или объединяются, чтобы отразить чье-то нападение. Детеныши объединяются со своими старшими сестрами. 
    Интересно, что маленький детеныш имеет в группе более высокий статус, чем его старшие сестры. Подросшие самцы, как 
    только покидают материнскую группу, теряют свой унаследованный статус, но они могут присоединиться к группе своих 
    старших братьев.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Арбузик 🍉':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_begemot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы КАРЛИКОВЫЙ БЕГЕМОТИК! Какой красавчик! Правда ведь?</b>''')
        text3 = ('''
    Интересный факт о КАРЛИКОВЫХ БЕГЕМОТАХ:
    Днём бегемоты, как правило, отлёживаются в воде или в прибрежных зарослях, с наступлением сумерек отправляются на 
    кормёжку. Растительная диета не калорийная, поэтому приходится есть много и на поедание корма у животных уходит не 
    меньше 6 часов в сутки. О социальной структуре популяции карликовых бегемотов в природе практически ничего не 
    известно, но встречаются они обычно поодиночке, иногда парами. Размер участка обитания взрослого самца около 2 кв. 
    км, самки – почти в четыре раза меньше. Исследователи отмечают, что при встречах животные не проявляют друг к другу 
    агрессии и не пытаются защищать свои участки. При опасности бегемотики, даже находясь рядом с водоёмом, не прячутся 
    в воде, а убегают в лесную чащу. Хищники, обитающие в тех же краях и способные добыть взрослого бегемота, - нильский
    крокодил и леопард. ''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Мороженное 🍦':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_sobol.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы СОБОЛЬ! Какой красавчик! Правда ведь?</b>''')
        text3 = ('''
    Интересный факт о СОБОЛЯХ:
    Активны соболи чаще в сумерках, но могут охотиться и ночью, и днём. Дневная активность заметно повышается во время 
    сезона размножения. Не считая сезона размножения, соболи ведут одиночный образ жизни. Границы своего охотничьего 
    участка соболь метит пахучим секретом, охраняет их, но нестрого. Нередко участки соседей значительно перекрываются, 
    изредка соболи даже могут использовать одни и те же временные убежища (но в разное время). Во время гона самец 
    преследует самку, самка обороняется, иногда завязывается довольно мирная игра. При вольерном разведении после 
    спаривания самка проявляет агрессию к самцу, и зверей рассаживают. Молодые зверьки ходят с самкой до конца лета, 
    затем выводок распадается.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Смотреть фильмы 📺':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_tulen.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы СЕРЫЙ ТЮЛЕНЬ! Вот это неожиданно 😉</b>''')
        text3 = ('''
    Интересный факт о СЕРЫХ ТЮЛЕНЯХ:
    У серых тюленей существуют две формы половых отношений: моногамия (1 самец и 1 самка), которая свойственна другим 
    видам настоящих тюленей, и полигамия (1 самец и несколько самок). В последнем варианте самец собирает гарем в 10–20 
    самок, и между самцами отмечаются драки. Однако самцы не очень ревностно относятся к своему гарему, и если 
    какая-нибудь самка уходит к другому самцу, он не пытается ее вернуть. В некоторых частях ареала (например, у 
    побережья Канады) полигамия не отмечена, а рядом с самкой и ее детенышем всегда держится 1 самец. Активность серых 
    тюленей дневная. В сумерках они становятся малоактивными; также они малоактивны и во время отливов. Вокализация в 
    жизни серых тюленей играет большую роль, особенно во время «залежек» на берегу. Когда самцы выясняют между собой 
    отношения из-за места, их рев слышен на очень большое расстояние.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Да не могу остановится 🤸🏼‍♂️':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_fenek.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ФЕНЕК! Он очень классный 😉</b>''')
        text3 = ('''
    Интересный факт о ФЕНЬКАХ:
    Фенек — обитатель пустыни, и для него, как и для многих других пустынных жителей, характерен ночной образ жизни. 
    Днём пустыня кажется безжизненной и пробуждается с заходом солнца. В это время суток воздух становится более 
    влажным, заметно сокращается испарение драгоценной воды из организма, и животные покидают норы. Фенеки живут 
    семейными группами, основу которой составляет размножающаяся пара. Подросшие лисята остаются с родителями на 
    следующий год и часто не покидают нору с появлением новых детёнышей. Возможно, старшие братья и сёстры помогают 
    родителям заботиться о малышах. По крайней мере, все много играют друг с другом, развивая ловкость и силу. Число 
    зверьков в такой группе доходит до 10.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Лучше поделать что то еще 🎮':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_pol_volk.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ПОЛЯРНЫЙ ВОЛК! Он очень классный 😉</b>''')
        text3 = ('''
    Интересный факт о ПОЛЯРНЫХ ВОЛКАХ:
    Волк – сильный, ловкий и умный хищник. Волки — сощиальные животные, живущие, как правило, семьями, состоящими из 
    6—10 разновозрастных особей, хотя иногда численность стаи может доходить и до 20. Основу ее составляет одна 
    размножающаяся пара. Кроме нее в стаю входят ее дети последнего («прибылые») и предпоследнего («переярки») пометов.
    Часто вместе с ними живет кто-то из более старших детей либо братьев или сестер кого-то из родителей (такие звери 
    остаются безбрачными, если только не найдут партнера и не покинут прежнюю семью). Вожака  в стае легко узнать по 
    высоко поднятому хвосту, для всех остальных подобная вольность недопустима.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Мне нравится есть на лету 🦅':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_pelican.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы КУДРЯВЫЙ ПЕЛИКАН! Он очень классный 😉</b>''')
        text3 = ('''
    Интересный факт о КУДРЯВЫХ ПЕЛИКАНАХ:
    Основная активность пеликанов приурочена к утренним и вечерним часам. Днём птицы, как правило, отдыхают. Кудрявые 
    пеликаны, как и другие, — птицы «компанейские», хорошо чувствуют себя только в сообществе себе подобных. Гнездятся 
    они небольшими колониями, часто совместно с розовыми пеликанами. Негнездящиеся птицы иногда живут вблизи колонии, но
    могут отлетать на довольно большие расстояния, к более рыбным угодьям. Дело в том, что во время гнездования 
    приоритет в выборе места отдаётся безопасности, и водоём может быть не очень богат рыбой. В послегнездовой период, 
    главным становится доступность корма, и пеликаны перебираются на наиболее богатые рыбой водоёмы.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Лучше спокойно дома 🍕':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_nutria.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы НУТРИЯ! 😉</b>''')
        text3 = ('''
    Интересный факт о НУТРИЯX:
    В природных условиях нутрии активны в основном ночью. Обычно они начинают активно кормиться перед заходом солнца, 
    причем сигналом для кормового поведения, возможно, служит именно снижение количества света. В дикой природе эти 
    зверьки живут большими группами, в состав такой группы входят взрослые самки разных возрастов, один доминантный 
    самец и многочисленное потомство. В больших группах иногда возникают еще и группки меньшего размера, состоящие в 
    основном из молодых или мелкими самцами. В одной группе отношения между животными миролюбивые, часто наблюдается 
    взаимопомощь: самки кормят детенышей друг друга, животные чистят друг другу шерсть (такое поведение носит название 
    аллогруминг), подают сигналы опасности. Конкурентные взаимодействия в группе редки, но один, наиболее сильный и 
    крупный самец постоянно поддерживает свой главенствующий статус.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Да стараюсь жить по режиму 🛌🏻':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_jiraf.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ЖИРАФ! 🦒</b>''')
        text3 = ('''
    Интересный факт о ЖИРАФАX:
    Жирафы — дневные животные. Обычно они кормятся утром и во вторую половину дня, а наиболее жаркие часы проводят в 
    полусне, стоя в тени акаций. В это время жирафы жуют жвачку, глаза их полуприкрыты, но уши находятся в постоянном 
    движении. Настоящий сон у жирафов ночью. Тогда они ложатся на землю, поджимая под себя передние ноги и одну из 
    задних, а голову кладут на другую заднюю ногу, вытянутую в сторону (вытянутая задняя нога позволяет жирафу быстро 
    подняться в случае приближения опасности). Длинная шея оказывается при этом изогнутой назад наподобие арки. Этот сон
    часто прерывается, животные встают, затем ложатся снова. Суммарная продолжительность полного глубокого сна у 
    взрослых животных поразительно мала: она не превышает 20 минут за всю ночь!''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


    if message.text == 'Все ни как не получится  🤦🏻':
        text1 = ('''<b>Ну вот наш тест подошел к концу! Еще немного нам нужно времени чтобы наконец то узнать кто же 
        ваше тотемное животное. Нам уже не терпится узнать, поскорей бы наш БОТ все правильно вычислил!</b>''')
        bot.send_message(message.chat.id, text1, parse_mode='HTML')
        time.sleep(10)
        photo1 = open('photo/result_filin.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        text2 = ('''<b>И вот какой результат теста: Вы ФИЛИН! 🦉</b>''')
        text3 = ('''
    Интересный факт о ФИЛИНАХ:
    Как у большинства сов активность филина сумеречная и ночная. Дневное время он предпочитает пережидать где-нибудь в 
    укрытии. Большую часть жизни филины проводят в одиночестве. Даже если самка и самец живут на общей территории, у 
    каждого из них свое убежище, и каждый охотится самостоятельно. Филины консервативны и, при наличии достаточного 
    количества корма, в течение всей жизни не покидают своего участка, площадь которого колеблется от 15 до 80 кв. км.''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn111 = types.KeyboardButton('Помочь своему тотемному животному ❤')
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn111, btn999, btn888)
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')


##guardianship logic  ##guardianship logic  ##guardianship logic  ##guardianship logic  ##guardianship logic  ##guardianship logic  ##guardianship logic  ##guardianship logic  ##guardianship logic
##⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇####⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇


    if message.text == 'Помочь своему тотемному животному ❤':
        text1 = (f'''<b>❤️ Вы можете стать опекуном любого животного в Московском зоопарке. Участие в программе «Возьми 
        животное под опеку» — это ваш личный вклад в дело сохранения биоразнообразия Земли и развитие нашего зоопарка. 
        Узнать подробности можно по телефону 📞 +7(958)813-15-60
        или написать нам на электронную почту: 📬 a.sharapova@moscowzoo.ru</b>''')

        photo1 = open('photo/opeka.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn888 = types.KeyboardButton('Оставить коментарий 💭')
        btn999 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn999, btn888)
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')

















