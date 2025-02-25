import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv("DATABASE_PATH", "my_database.sqlite")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)


def connect_db():
    try:
        session = Session()

        print(f"Успішно підключено до бази даних SQLite за адресою: {DATABASE_PATH}")
        return session

    except Exception as e:
        print(f"Не вдалося підключитися до бази даних: {e}")
        return None
