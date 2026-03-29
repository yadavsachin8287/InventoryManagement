from fastapi import FastAPI
from models import product
# from app.database import SessionLocal, engine 
#import database_models


app = FastAPI()
  
#database_models.Base.metadata.create_all(bind=engine)
@app.get("/")
def green():
    return "welcome to my api"
   
products=[
    product(id=1, name="laptop", description="gaming laptop", price=50000, quantity=10),
    product(id=2, name="mobile", description="gaming mobile", price=30000, quantity=20),
    product(id=5, name="headphone", description="gaming headphone", price=5000, quantity=30),
    product(id=4, name="keyboard", description="gaming keyboard", price=2000, quantity=40),
]

@app.get("/products")
def get_all_products():
 
 return products   

@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
           return product
    return {"message": "product not found"}     

@app.post("/products")
def add_product(product: product):
    products.append(product)
    return {"message": "product added successfully"}

@app.put("/products/{id}")
def update_product(id: int, updated_product: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = updated_product
            return {"message": "product updated successfully"}
    return {"message": "product not found"}

@app.delete("/products/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return {"message": "product deleted successfully"}
    return {"message": "product not found"}
