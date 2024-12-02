## from typing import Optional
## from fastapi.responses import JSONResponse
#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/")
#async def root():
   # return JSONResponse({"message": "Hello World"})

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
 #   return {"item_id": item_id, "q": q}

from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# MongoDB connection (replace with your connection string)
client = MongoClient("<your_mongodb_connection_string>")
db = client["your_database_name"]
collection = db["your_collection_name"]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def read_items():
    items = []
    async for item in collection.find():
        items.append(item)
    return items

@app.post("/items")
async def create_item(item: dict):
    result = collection.insert_one(item)
    return {"inserted_id": str(result.inserted_id)}

# ... other endpoints for CRUD operations
