from sqlalchemy.orm import Session
from models import User, Product

# -------------------------
# CRUD Users
# -------------------------
def create_user(db: Session, name: str, email: str, age: int):
    user = User(name=name, email=email, age=age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session):
    return db.query(User).all()

# -------------------------
# CRUD Products
# -------------------------
def create_product(db: Session, name: str, price: float, quantity: int):
    product = Product(name=name, price=price, quantity=quantity)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session):
    return db.query(Product).all()
