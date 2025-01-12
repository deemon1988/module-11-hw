import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Вставьте ваш токен
API_TOKEN = '7810014291:AAGFYOO3Ed9_F86T2H4yShgt1RDdMBl1kWQ'
bot = telebot.TeleBot(API_TOKEN)

# Список напитков
drinks_menu = {
    "Кока-Кола": 100,
    "Пепси": 90,
    "Сок": 80,
    "Вода": 50
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для продажи напитков. Выберите напиток из меню ниже:', reply_markup=create_drinks_keyboard())

def create_drinks_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for drink in drinks_menu.keys():
        button = KeyboardButton(drink)
        markup.add(button)
    return markup

@bot.message_handler(func=lambda message: message.text in drinks_menu)
def order(message):
    drink = message.text
    bot.send_message(message.chat.id, f'Вы заказали {drink}. Спасибо за покупку!')

@bot.message_handler(func=lambda message: True)
def unknown_message(message):
    bot.send_message(message.chat.id, 'Пожалуйста, выберите напиток из меню или введите /start для начала.')

# Запуск бота
bot.polling(none_stop=True)