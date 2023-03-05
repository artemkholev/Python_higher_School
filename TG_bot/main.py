import telebot
from random import *
from telebot import types


#   TOKEN
bot = telebot.TeleBot('5577592724:AAF2fcvRQzmtd4ABU1m6RMt7kvIWpUVXHtk')

# НАЧАЛЬНЫЕ КОМАНДЫ
@bot.message_handler(commands=['start'])
def start(message):
    mes = False
    if not mes:
        txt = message.text
        messege = f'Привет <b>{message.from_user.first_name} {message.from_user.last_name}</b> , для про должения введите сколько вам лет?'
        msg = bot.send_message(message.chat.id, messege, parse_mode='html')
        bot.register_next_step_handler(msg, askage)
        mes = True

def askage(message):
    txt = message.text
    if not txt.isdigit():
        msg = bot.send_message(message.chat.id, 'Введите возраст цифрами (например: 12).')
        bot.register_next_step_handler(msg, askage)
        return
    if int(txt) > 10 and int(txt) < 100:
        msg = bot.send_message(message.chat.id, f'Я запомнил твой возраст, {txt} лет.')
        mes = False
    else:
        msg = bot.send_message(message.chat.id, 'Ограничение возраста от 10 лет до 100. Введите в этом диапозоне.')
        bot.register_next_step_handler(msg, askage)
        return


# БЛИНЫ
@bot.message_handler(commands=['take'])
def start1(message):
    photo = open('photo.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить вэб сайт.', url="https://www.russianfood.com/recipes/recipe.php?rid=133122"))
    bot.send_message(message.chat.id, 'Нажми, чтобы перейти на веб сат.', reply_markup=markup)

# КОМАНДЫ
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    save = message.text.lower()
    s = ['Я пока не понимаю тебя.', 'Я не могу на это ответить.', 'Скоро я научусь это делать.', 'Я не понимаю.', 'Не могу на это ответить.', 'Для меня команда пока не известна.']
    if save == 'id':
        bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}', parse_mode='html')
        # bot.send_message(message.chat.id, message, parse_mode='html')
    elif save == 'привет':
        bot.send_message(message.chat.id, 'Добро пожаловать, меня зовут Keny.')
    else:
        bot.send_message(message.chat.id, s[randint(0, len(s)) - 1], parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_text(message):
    bot.send_message(message.chat.id, 'Красиво!', parse_mode='html')
bot.polling(none_stop=True)