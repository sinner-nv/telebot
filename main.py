import telebot
from telebot import types


TOKEN = None
with open('token.txt', 'r') as file:
    TOKEN=file.read().strip()
bot = telebot.TeleBot(TOKEN)


def list_ofd(ofd_name):

   ofd_spisok = {
        'такском': ['ООО \"Такском\"', '7704211201', '193.0.214.11', 'f1.taxcom.ru', '7777', 'noreply@taxcom.ru', 'f1.taxcom.ru', '8777'],
        'офд': ['ООО \"ПС СТ\"', '7841465198', '94.143.160.11', 'gate.ofd.ru', '4001', 'feedback@ofd.ru', 'crpt.ofd.ru', '7000'],
        'первый': ['ООО \"Первый ОФД\"', '7709364346', '91.107.114.010', 'k-server.1-ofd.ru', '7777', 'info@1-ofd.ru', 'k-server.1-ofd.ru', '7788'],
        'платформа': ['ООО \"Эвотор ОФД\"', '9715260691', '185.170.204.091', 'ofdp.platformaofd.ru', '21101', 'info@platformaofd.ru', 'ofdp.platformaofd.ru', '21102'],
        'ярус': ['ООО \"Ярус\"', '7728699517', '091.107.067.212', 'connect.ofd-ya.ru', '7779', 'help@ofd-ya.ru', 'connect.ofd-ya.ru', '7797'],
        'яндекс': ['ООО \"Яндекс ОФД\"', '7704358518', '185.032.186.252', 'kkt.ofd.yandex.net', '12345', 'askofd@support.yandex.ru', 'kkt.ofd.yandex.net', '54321'],
        'астрал': ['ЗАО \"Калуга Астрал\"', '4029017981', '091.239.005.068', 'ofd.astralnalog.ru', '7777', 'client@astralnalog.ru', 'ofd.astralnalog.ru', '7777'],
        'сбис': ['ООО \"Компания "ТЕНЗОР\"', '7605016030', '091.213.144.029', 'kkt.sbis.ru', '7777', 'noreply@sbis.ru', 'kkt.sbis.ru', '7777'],
        'гарант': ['ООО \"Электронный Экспресс\"', '7729633131', '141.101.203.186', 'ofd.garantexpress.ru', '30801', 'ee@garant.ru', '-', '-'],
        'крокус': ['ООО \"КОРУС Консалтинг СНГ\"', '7801392271', '92.38.2.200', '-', '7001','help@esphere.ru ', '-', '-'],
        'контур': ['ООО \"Контур НТТ\"', '6658497833', '046.017.204.250', 'ofd.kontur.ru', '7777', 'noreply@kontru.ru', 'ofd.kontur.ru', '7778'],
        'инитпро': ['ООО \"Удостоверяющий центр \"ИнитПро\"\"', '5902034504', '-', 'ofd-initpro.ru', '9999', '-', '-', '-'],
        'е-офд': ['ООО \"Группа Элемент\"', '7729642175', '176.122.030.030', 'kkt.e-ofd.ru', '7777', 'reciept@e-ofd.ru', '-', '-'],
    }
   if ofd_name in ofd_spisok:
       return ofd_spisok[ofd_name]
   else:
       return f'ОФД {ofd_name} нет!!!'


@bot.message_handler(content_types=['text'])
def get_ofd(message):
   if message.text == '/help':
       bot.send_message(message.from_user.id, 'Напиши привет')
   else:
       keyboard = types.InlineKeyboardMarkup()
       key_1 = types.InlineKeyboardButton(text='ООО \"Такском\"', callback_data='такском')
       key_2 = types.InlineKeyboardButton(text='ООО \"ПС СТ\"', callback_data='офд')
       key_3 = types.InlineKeyboardButton(text='ООО \"Первый ОФД\"', callback_data='первый')
       key_4 = types.InlineKeyboardButton(text='ООО \"Эвотор ОФД\"', callback_data='платформа')
       key_5 = types.InlineKeyboardButton(text='ООО \"Ярус\"', callback_data='ярус')
       key_6 = types.InlineKeyboardButton(text='ООО \"Яндекс ОФД\"', callback_data='яндекс')
       key_7 = types.InlineKeyboardButton(text='ЗАО \"Калуга Астрал\"', callback_data='астрал')
       key_8 = types.InlineKeyboardButton(text='ООО \"Компания "ТЕНЗОР\"', callback_data='сбис')
       key_9 = types.InlineKeyboardButton(text='ООО \"Электронный Экспресс\"', callback_data='гарант')
       key_10 = types.InlineKeyboardButton(text='ООО \"КОРУС Консалтинг СНГ\"', callback_data='крокус')
       key_11 = types.InlineKeyboardButton(text='ООО \"Контур НТТ\"', callback_data='контур')
       key_12 = types.InlineKeyboardButton(text='ООО \"Удостоверяющий центр \"ИнитПро\"\"', callback_data='инитпро')
       key_13 = types.InlineKeyboardButton(text='ООО \"Группа Элемент\"', callback_data='е-офд')
       keyboard.add(key_1)
       keyboard.add(key_2)
       keyboard.add(key_3)
       keyboard.add(key_4)
       keyboard.add(key_5)
       keyboard.add(key_6)
       keyboard.add(key_7)
       keyboard.add(key_8)
       keyboard.add(key_9)
       keyboard.add(key_10)
       keyboard.add(key_11)
       keyboard.add(key_12)
       keyboard.add(key_13)
       bot.send_message(message.chat.id, 'Выбери ОФД', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    set_ofd = list_ofd(call.data)
    msg_taxcom = 'Название: {0}\n' \
                 'ИНН:           {1}\n' \
                 'IP адрес ОФД:    {2}\n' \
                 'DNS имя ОФД:   {3}\n' \
                 'Порт ОФД:          {4}\n' \
                 'EMAIL:        {5} ' \
                 'DNS имя КМ:          {6}\n' \
                 'Порт ОФД:        {7} '.format(set_ofd[0], set_ofd[1], set_ofd[2], set_ofd[3], set_ofd[4], set_ofd[5], set_ofd[6], set_ofd[7])
    bot.send_message(call.message.chat.id, msg_taxcom)


bot.polling(none_stop=True, interval=0)