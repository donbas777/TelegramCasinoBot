import os
import telebot
from telebot import types
from controllers.user_controllers import add_user, image_folder, get_balance


TOKEN = os.getenv('TOKEN')
print(TOKEN)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    username = message.from_user.username or "Unknown"
    add_user(chat_id, username)
    markup = types.InlineKeyboardMarkup()
    balance = get_balance(chat_id)

    photo_path = os.path.join(image_folder, "start_image.webp")
    text = (
        f"🎰 Добро пожаловать в наше эксклюзивное казино! 🎲\n\n"
        f"🔹 Ваш ID: `{chat_id}`\n"
        f"💰 Баланс: `{balance}` кредитов\n\n"
        f"🚀 Испытайте удачу и сорвите крупный куш!\n\n"
        f"📍 Выберите действие в меню ниже:"
    )
    with open(photo_path, "rb") as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=text,
            reply_markup=markup,
            parse_mode="Markdown"
        )

bot.polling(none_stop=True)