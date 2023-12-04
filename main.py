from fastapi import FastAPI
from care import Carewoche

app = FastAPI()
#> uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Here goes Carewoche"}

@app.get("/members/")
async def read_item(skip: int = 0, limit: int = 10):
    c = Carewoche('test/resource_t1.json')
    l = list(c.getMembers().items())
    ol = l[skip: skip + limit]
    return dict(ol)

@app.get("/order/")
async def read_item(skip: int = 0, limit: int = 10):
    c = Carewoche('test/resource_t1.json')
    return c.getOrder()[skip: skip + limit]
    