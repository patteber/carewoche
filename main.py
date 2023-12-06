import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from care import Carewoche
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.mount('/static', StaticFiles(directory='static',html=True))
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
#> uvicorn main:app --reload
class Member(BaseModel):
    name: str
    active: bool = True

class changeOrder(BaseModel):
    name: str
    offset: int

@app.get("/")
async def root():
    return {"Service Name": "CareWocheService"}

@app.get("/members/")
async def read_members(skip: int = 0, limit: int = 10):
    c = Carewoche('test/resource_t2.json')
    l = list(c.getMembers().items())
    ol = l[skip: skip + limit]
    return dict(ol)

@app.post("/members/", status_code=201)
async def add_member(member: Member):
    c = Carewoche('test/resource_t2.json')
    c.postMember(member.name, member.active)
    c.writeFile()
    return c.getMembers()

@app.delete("/members/")
async def delete_member(member: Member):
    c = Carewoche('test/resource_t2.json')
    c.deleteMember(member.name)
    c.writeFile()
    return c.getMembers()

@app.get("/order/")
async def read_order(skip: int = 0, limit: int = 10):
    c = Carewoche('test/resource_t2.json')
    return c.getOrder()[skip: skip + limit]

@app.post("/order/change/")
async def change_order(co: changeOrder):
    d = co.model_dump()
    c = Carewoche('test/resource_t2.json')
    try:
        c.changeMembersOrder(d.get("name"), d.get("offset"))
    except ValueError:
        raise HTTPException(status_code=404, detail="Name not found")

    c.writeFile()
    return c.getOrder()

@app.post("/order/iterate/")
async def change_order():
    c = Carewoche('test/resource_t2.json')
    c.iterateOrder()
    c.writeFile()
    return c.getOrder()