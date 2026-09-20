from fastapi import FastAPI
import database_models
from database import engine

app=FastAPI()

database_models.Base.metadata.create_all(bind=engine)
@app.get("/product")
def get_all_products():
    return "all products are returned"
