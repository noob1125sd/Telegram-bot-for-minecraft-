import telebot
from mcrcon import MCRcon
import re

rcon = MCRcon("ip", "password", port=25575)
rcon.connect()

bot = telebot.TeleBot("BOT_TOKEN")
IDs = [] #
# buttons
@bot.callback_query_handler(func=lambda callback: True)
def info(callback):
    bot.answer_callback_query(callback.id)
    if callback.data == "info":
        # info
        bot.send_chat_action(callback.message.chat.id, 'typing')
        server_online = rcon.command("list")
        parsed_online = re.findall(r'\d+\b', server_online)

        information = f"""<b>Информация о сервереℹ️

Текущий Онлайн: {parsed_online[0]}/{parsed_online[2]}{parsed_online[3]}

Хозяева Сервера: 
HAOSEMASTER и YaAngel4

ip Сервера: gf-1.apexnodes.xyz:26255

Правила:
1: Не читерить
2: Не обманывать
3: Не оскать админов
4: Афк не более 30 минут
5: Веселиться! </b>
        """

        markup = telebot.types.InlineKeyboardMarkup()
        btn0 = telebot.types.InlineKeyboardButton("Назад", callback_data="back")
        markup.row(btn0)

        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

        bot.send_message(callback.message.chat.id, information, parse_mode="html", reply_markup=markup)

    elif callback.data == "adminpanel":
        #panel
        if callback.from_user.id in IDs:
            bot.send_message(callback.message.chat.id, "Права есть")
        else:
            bot.send_message(callback.message.chat.id, "Нет прав")
            print(callback.from_user.id)
    # donate(not finished)
    elif callback.data == "donate":
        bot.send_message(callback.message.chat.id, "Донат")
    
    elif callback.data == "back":

        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

        btnpnl = telebot.types.InlineKeyboardMarkup()
        btn0 = telebot.types.InlineKeyboardButton('Информация о сервере ℹ️', callback_data="info")
        btn1 = telebot.types.InlineKeyboardButton('Донат 💰', url="")
        btn2 = telebot.types.InlineKeyboardButton('ТГК сервера 📢', url="")
        btn3 = telebot.types.InlineKeyboardButton("Чат сервера 💬", url="")
        btn4 = telebot.types.InlineKeyboardButton("RCON панель ⚙️", callback_data='adminpanel')
        btnpnl.row(btn0)
        btnpnl.row(btn2, btn3)
        btnpnl.row(btn1, btn4)
        menu_text = f"""<b>{callback.from_user.first_name}, Привет👋🏻! 
Я бот Minecraft сервера,
Здесь можно:
• Посмотреть правила
• Посмотреть Онлайн
• Доступные донаты и их функции
• Перейти в ТГК и Чат сервера.</b>"""
        bot.send_message(callback.message.chat.id, text=menu_text, reply_markup=btnpnl, parse_mode="html")
      
@bot.message_handler()
def sendmessage(message):
    if message.text == "/start":
        btnpnl = telebot.types.InlineKeyboardMarkup()
        btn0 = telebot.types.InlineKeyboardButton('Информация о сервере ℹ️', callback_data="info")
        btn1 = telebot.types.InlineKeyboardButton('Донат 💰', url="")
        btn2 = telebot.types.InlineKeyboardButton('ТГК сервера 📢', url="")
        btn3 = telebot.types.InlineKeyboardButton("Чат сервера 💬", url="")
        btn4 = telebot.types.InlineKeyboardButton("RCON панель ⚙️", callback_data='adminpanel')
        btnpnl.row(btn0)
        btnpnl.row(btn2, btn3)
        btnpnl.row(btn1, btn4)
        menu_text = f"""<b>{message.from_user.first_name}, Привет👋🏻! 
Я бот Minecraft сервера OceanMine,
Здесь можно:
• Посмотреть правила
• Посмотреть Онлайн
• Доступные донаты и их функции
• Перейти в ТГК и Чат сервера.</b>"""
        bot.send_message(message.chat.id, text=menu_text, reply_markup=btnpnl, parse_mode="html")

bot.infinity_polling()
