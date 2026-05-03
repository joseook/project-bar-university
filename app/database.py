import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Carrega as variáveis do arquivo .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Monta a URL de conexão com o PostgreSQL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Cria a engine (motor de conexão com o banco)
engine = create_engine(DATABASE_URL)

# Cria a sessão — é por ela que executamos queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Classe base para todos os models (tabelas)
class Base(DeclarativeBase):
    pass


# Função auxiliar usada nas rotas para abrir e fechar a sessão corretamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
