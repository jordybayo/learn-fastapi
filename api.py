from fastapi import FastAPI, Form

import uvicorn

from typing import Optional

from pydantic import BaseModel

app = FastAPI()


class CoordIn(BaseModel):
    password : str
    lat  : float
    lon  : float
    zoom : Optional[int] = None
    description: Optional[int] = None

class CoordOut(BaseModel):
    lat  : float
    lon  : float
    zoom : Optional[int] = None
    description: Optional[int] = None


# get, put, delete, 

#get
@app.get("/")
async def hello_world():
    return {"hello" : "world"}



@app.post("/position/", response_model=CoordOut, response_model_exclude={'description'})
async def make_position(coord: CoordIn):
    # db write completed
    return coord


@app.get("/component/{component_id}") # path parameter
async def get_component(component_id: int):
    # operations 
    return {"component" : component_id}



@app.post("/login/")
async def login(username: str = Form(...), password: str= Form(...)):
    return {username: username}






@app.get("/component/")
async def read_component(number: int, text: Optional[str]):
    return {"number" : number, "text": text}

# # http://127.0.0.1:8000/component/?number=12&text=component%20name

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)