from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(String(50), unique=True, nullable=False)
    username = Column(String(50), nullable=True)
    balance = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
