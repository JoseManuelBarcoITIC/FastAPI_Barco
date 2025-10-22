from dotenv import load_dotenv
from fastapi import FastAPI,Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Field, Session

from FastAPI_Barco.models.User import User
from models.Product import Product, ProductRequest

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
@app.get("/user/{id}", response_model = dict, tags = ["READ BY ID"])
def getUser(product: ProductRequest,db:Session = Depends(get_db)):
    stmt = select(Product).where(Product.id == product.id)
    result = db.exec(stmt).scalar()
    print(result)
    return UserResponse.model_validate(result)

