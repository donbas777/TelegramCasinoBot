import os
from db.models import User
from telebot import types
from db.database import Session


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_folder = os.path.join(BASE_DIR, "bot_images")


def add_user(chat_id, username):
    session = Session()
    existing_user = session.query(User).filter_by(chat_id=str(chat_id)).first()
    if not existing_user:
        new_user = User(chat_id=str(chat_id), username=username)
        session.add(new_user)
        session.commit()
        print(f"User {username} added to the database.")
    else:
        print(f"User {username} already exists in the database.")
    session.close()


def get_balance(chat_id):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(chat_id)).first()
    return user.balance

def get_users_count():
    session = Session()
    result = session.query(User).count()
    session.close()

    return f"Кількість користувачів: {result}"

def get_users():
    session = Session()
    users = session.query(User).all()  # Отримуємо всіх користувачів із бази
    session.close()
    return users

