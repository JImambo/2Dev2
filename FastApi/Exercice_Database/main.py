from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud, models

# Crée les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI avec Users et Products")

# -------------------------
# Dépendance pour obtenir DB
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API FastAPI Users & Products"}

# -------------------------
# Routes Users
# -------------------------
@app.post("/users/")
def api_create_user(name: str, email: str, age: int, db: Session = Depends(get_db)):
    return crud.create_user(db, name, email, age)

@app.get("/users/")
def api_get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# -------------------------
# Routes Products
# -------------------------
@app.post("/products/")
def api_create_product(name: str, price: float, quantity: int, db: Session = Depends(get_db)):
    return crud.create_product(db, name, price, quantity)

@app.get("/products/")
def api_get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)
