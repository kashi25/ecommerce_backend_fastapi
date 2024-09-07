
from sqlalchemy.orm import Session
from app import models, schemas

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, price=product.price, description=product.description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
    