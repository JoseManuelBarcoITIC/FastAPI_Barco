from dotenv import load_dotenv
from fastapi import FastAPI,Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Field, Session, select, delete

from models.User import User
from models.Product import Product, ProductRequest,ProductResponse, ProductResponsePartial

import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def get_db():
    db= Session(engine)
    try:
        yield db
    finally:
        db.close()
app = FastAPI()

@app.post("/product", response_model = dict, tags = ["CREATE"])
def add_user(product: ProductRequest,db:Session = Depends(get_db)):
    insert_product = Product.model_validate(product)
    db.add(insert_product)
    db.commit()
    return {"msg":"Afegit usuari correctament"}
@app.get("/product/{id}", response_model=ProductResponse, tags = ["GETS"])
def Get_Product_By_Id(id:int ,db:Session = Depends(get_db)):
    stmt = select(Product).where(Product.id == id)
    result = db.exec(stmt).first()
    return ProductResponse.model_validate(result)
@app.get("/products", response_model=list[ProductRequest], tags = ["GETS"])
def Get_Product_List(db:Session = Depends(get_db)):
    stmt = select(Product)
    result = db.exec(stmt).all()
    return result
@app.get("/products/{price}", response_model=list[ProductRequest], tags = ["GETS"])
def Get_All_Products_List_By_Price(price:int,db:Session = Depends(get_db)):
    stmt = select(Product).where(Product.price == price)
    result = db.exec(stmt).all()
    return result
@app.get("/productspartial", response_model=list[ProductResponsePartial], tags = ["GETS"])
def Get_All_Products_Partial(db:Session = Depends(get_db)):
    stmt = select(Product)
    result = db.exec(stmt).all()
    return result
@app.delete("/products/{id}", response_model=dict, tags = ["DELETES"])
def Delete_Product(id:int,db:Session = Depends(get_db)):
    stmt = delete(Product).where(Product.id == id)
    result = db.exec(stmt)
    db.commit()
    return {"msg":"Usuari eliminat correctament"}