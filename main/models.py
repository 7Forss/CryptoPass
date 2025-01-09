from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    telegram_id = Column(Integer, unique=True)
    wallet_id = Column(Integer, ForeignKey('wallets.id'))
    wallet = relationship("Wallet", back_populates="user")
    total_points = Column(Integer, default=0)
    rank = Column(String)

class Wallet(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True)
    address = Column(String, unique=True)
    user = relationship("User", back_populates="wallet")
    statistics = relationship("Statistics", back_populates="wallet")

class Statistics(Base):
    __tablename__ = 'statistics'
    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey('wallets.id'))
    wallet = relationship("Wallet", back_populates="statistics")
    transactions_count = Column(Integer, default=0)
    total_received = Column(Float, default=0.0)
    total_sent = Column(Float, default=0.0)
    balance = Column(Float, default=0.0)
    points = Column(Integer, default=0)

class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(String)
    points = Column(Integer)
    user = relationship("User")

# Инициализация базы данных
engine = create_engine('sqlite:///crypto_passport.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()