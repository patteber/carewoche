from fastapi import FastAPI
from care import Carewoche
from pydantic import BaseModel

app = FastAPI()
#> uvicorn main:app --reload

@app.get("/")
async def root():
    return {"Service Name": "CareWocheService"}

@app.get("/members/")
async def read_members(skip: int = 0, limit: int = 10):
    c = Carewoche('test/resource_t2.json')
    l = list(c.getMembers().items())
    ol = l[skip: skip + limit]
    return dict(ol)
# post/put member, see https://realpython.com/api-integration-in-python/#fastapi

@app.get("/order/")
async def read_order(skip: int = 0, limit: int = 10):
    c = Carewoche('test/resource_t2.json')
    return c.getOrder()[skip: skip + limit]

    
class changeOrder(BaseModel):
    ID: int
    offset: int
    
@app.post("/order/change/")
async def change_order(co: changeOrder):
    d = co.model_dump()
    c = Carewoche('test/resource_t2.json')
    c.changeMembersOrder(d.get("ID"), d.get("offset"))
    c.writeFile()
    return c.getOrder()

@app.post("/order/iterate/")
async def change_order():
    c = Carewoche('test/resource_t2.json')
    c.iterateOrder()
    c.writeFile()
    return c.getOrder()