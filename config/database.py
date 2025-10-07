import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from models import Base  # importa todos los modelos desde __init__.py


# 🧩 Cargar variables desde el archivo .env
load_dotenv()

# 📦 Leer variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# 🔗 Construir la URL de conexión
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 🔌 Crear el engine
engine = create_engine(DATABASE_URL, echo=True)

# 🧩 Crear la sesión
SessionLocal = scoped_session(sessionmaker(bind=engine))
