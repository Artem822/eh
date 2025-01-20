from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Определяем URL PostgreSQL
postgresql_url = 'postgresql://postgres:11111@localhost:5432/zadanie'

# Создаём движок
engine = create_engine(postgresql_url)

# Устанавливаем соединение
connection = engine.connect()

Session = sessionmaker(bind=engine)


