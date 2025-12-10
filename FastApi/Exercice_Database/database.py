from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# -------------------------------
# CONFIGURATION DE LA BASE DE DONNÉES
# -------------------------------
# SQLite (par défaut)
DATABASE_URL = "sqlite:///./test.db"

# MySQL (exemple MAMP)
# DATABASE_URL = "mysql+pymysql://root:root@localhost:8889/mabase"

# Engine SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Session pour les requêtes
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base pour les modèles
Base = declarative_base()

# -------------------------------
# Fonction utilitaire pour tests
# -------------------------------
def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            print(f"Test réussi. SELECT 1 -> {result.scalar()}")
    except Exception as e:
        print("Erreur connexion :", e)

if __name__ == "__main__":
    test_connection()
