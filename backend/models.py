from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True, nullable=False)
    name = Column(String)
    photo = Column(String)
    binance_api = Column(String)
    binance_secret = Column(String)
    level = Column(Integer, default=1)

class Signal(Base):
    __tablename__ = "signals"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    symbol = Column(String)
    type = Column(String)
    price = Column(Numeric)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String)

class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    signal_id = Column(Integer, ForeignKey("signals.id"))
    pnl = Column(Numeric)
    amount = Column(Numeric)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Level(Base):
    __tablename__ = "levels"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    exp = Column(Integer, default=0)
    level = Column(Integer, default=1)
