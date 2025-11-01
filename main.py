from dotenv import load_dotenv
from fastapi import FastAPI,Depends
from sqlalchemy import create_engine, update
from sqlmodel import SQLModel, Session, select, delete
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
    return {"msg":"Afegit producte correctament"}

@aspp.get("/product/{id}", response_model=ProductResponse, tags = ["GETS"])
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
    db.exec(stmt)
    db.commit()
    return {"msg":"Producte eliminat correctament"}

@app.put("/products/put/{id}", response_model=dict, tags = ["UPDATES"])
def Update_Product(id:int, product:ProductRequest,db:Session = Depends(get_db)):
    update_product = product.model_dump()
    stmt = (
        update(Product)
        .where(Product.id == id)
        .values(update_product)
    )
    db.exec(stmt)
    db.commit()
    return {"msg":"Producte modificat correctament"}

@app.patch("/products/patch/price/{id}", response_model=dict, tags = ["UPDATES"])
def Update_Price_Product(id:int,price: int,db:Session = Depends(get_db)):
    stmt = (
        update(Product)
        .where(Product.id == id)
        .values(price = price)
    )
    db.exec(stmt)
    db.commit()
    return {"msg":"Preu del producte modificat correctament"}

@app.patch("/products/patch/{id}", response_model=dict, tags = ["UPDATES"])
def Update_Partial_Product(product_id:int,price: int,name:str,db:Session = Depends(get_db)):
    stmt = (
        update(Product)
        .where(Product.id == product_id)
        .values(price = price, name = name)
    )
    db.exec(stmt)
    db.commit()
    return {"msg":"Nom i preu del producte modificat correctament"}