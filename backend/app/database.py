from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    brand = Column(String)
    price = Column(Float)
    category = Column(String)
    description = Column(String)

def get_product_data(query: str):
    session = SessionLocal()
    products = session.query(Product).filter(Product.name.ilike(f"%{query}%")).all()
    product_info = [f"{product.name} - {product.brand} - {product.price}" for product in products]
    return "\n".join(product_info)
