import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Туры по Беларуси")
item2 = types.KeyboardButton("Джип туры за границу")
item3 = types.KeyboardButton("Календарь туров")

markup.add(item1, item2, item3)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nНиже Вы можете выбрать подходящий для Вас "
                                      "тур и ознакомиться с расписанием "
                                      "предстоящих туров.".format (message.from_user, bot.get_me () ), parse_mode ='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Туры по Беларуси":
            bot.send_message(message.chat.id,
                               'Ближайшие туры выходного дня по РБ:\n\n-Байдарки + поход на болото + '
                               'усадьба\nhttps://psixtravel.by/tour/splav-boloto/ '
                               '\n\n-Сплав по рекам Узлянка-Нарочанка\nhttps://psixtravel.by/tour/splav-uzljanka'
                               '-narochanka/\n\n-Сплав! Бацька Нёман!\n '
                               'https://psixtravel.by/tour/splav-papa-neman/\n\n-Джип тур  '
                               '"War"\nhttps://psixtravel.by/tour/jeep-tour-war/')


            # photo = open ( 'Belarus_photo.jpg', 'rb' )
            # bot.send_photo ( message.from_user.id, photo )
        elif message.text == "Джип туры за границу":
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton("Джип тур в Карелию", callback_data='karelia')
            btn2 = types.InlineKeyboardButton("Джип туры в Молдову", callback_data='moldova')
            btn3 = types.InlineKeyboardButton("Джип туры в Грузию", callback_data='georgia')
            btn4 = types.InlineKeyboardButton("Бас тур 'Зимняя Карелия'", callback_data='wkarelia')
            markup.add(btn1, btn2, btn3, btn4)

            bot.send_message(message.chat.id, 'Ниже все текущие туры за границу:', reply_markup=markup)

        elif message.text == "Календарь туров":

            bot.send_message(message.chat.id, 'Для просмотра календаря перейдите по ссылке:\n'
                                              '-->https://docs.google.com/spreadsheets/d/e/2PACX-1vRc3rzf-0SY580lMQA2kidCHbr9_Eu-hctYd5EPIGY6DoYiQYliFiWrx-XhCjjq_CxwHtpBfHNNqLGd/pubhtml?gid=293021810&single=true')

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'karelia':
                bot.send_message(call.message.chat.id, "Джип тур в Карелию (12 дней - 3700 км.)\n🎈Без визы.\nhttps://psixtravel.by/tour/jeep-tur-karelia/")
            elif call.data == 'moldova':
                bot.send_message(call.message.chat.id, 'Джип тур в Молдову (6дней - 2400км)\n🎈Без визы.\nhttps://psixtravel.by/tour/jeep-tour-moldova/')
            elif call.data == 'georgia':
                bot.send_message(call.message.chat.id, '🚜Джип тур:\n1️⃣Тур в Грузию (7600 км - 15 дней)\nhttps://psixtravel.by/tour/4h4-gruzija/\n\n✈️🚜Авиа Джип тур:\n2️⃣Тур в Грузию 10 дней.\nhttps://psixtravel.by/tour/avia-gruzija/')
            elif call.data == 'wkarelia':
                bot.send_message(call.message.chat.id, 'Tур в Карелию🎁\n⌛8 дней - 3200 км.\nhttps://psixtravel.by/tour/tur-v-kareliju-zimnjaja-skazka/')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= "Выберите  подходящий тур для Вас:", reply_markup=None)

            # show alert
            # bot.answer_callback_query ( callback_query_id=call.id, show_alert=False,
            #                             text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!" )
    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)
