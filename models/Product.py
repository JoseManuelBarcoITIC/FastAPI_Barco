from sqlmodel import SQLModel,Field

class Product(SQLModel, table=True):
    id: int |None = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    quantity: int
    category: str

class ProductRequest(SQLModel):
    name: str
    description: str
    price: float
    quantity: int
    category: str

class ProductResponse(SQLModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    category: str
