import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Récupère l'URL de connexion depuis la variable d'environnement DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
# Exemples d'URL :
DATABASE_URL = "mysql+pymysql://root:root@localhost:8889/mabase"
# SQLite (fichier local) : sqlite:///./test.db
# MySQL (pymysql) : mysql+pymysql://user:password@host:3306/dbname
# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

def get_engine(url: str = DATABASE_URL):
    """
    Crée et retourne un engine SQLAlchemy.
    """
    # echo=True pour logs SQL (débogage), à désactiver en production
    return create_engine(url, echo=False, future=True)

def test_connection(engine):
    """
    Teste la connexion en exécutant SELECT 1 et retourne la valeur renvoyée.
    """
    try:
        with engine.connect() as conn:
            # exécute une requête simple
            result = conn.execute(text("SELECT 1"))
            # scalar() retourne la première colonne de la première ligne
            value = result.scalar()
            print(f"Test réussi. SELECT 1 -> {value}")
            return value
    except SQLAlchemyError as e:
        # Gestion d'erreur basique : affiche l'erreur et retourne None
        print("Erreur lors du test de connexion :", e)
        return None

if __name__ == "__main__":
    eng = get_engine()
    test_connection(eng)
