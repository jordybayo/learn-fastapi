from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()


templates = Jinja2Templates(directory="templates")

@app.get("/book/{id}", response_class=HTMLResponse)
async def read(requests: Request, book: str, id: int):
    return templates.TemplateResponse("index.html", {"request": requests, "book": book, "id": id})


