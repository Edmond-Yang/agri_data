from fastapi import FastAPI
from fastapi import Body, FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import uvicorn
from typing import Optional
from pydantic import BaseModel
from api import pdfAPI
import time

class Item(BaseModel):
    article: str
    content: str

app = FastAPI(
    title="Open-Domain Parrot Paragraph",
    description="Open-Domain Parrot Paragraph",
    version="0.1.0"
)

api = pdfAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def write_json(maps: dict):
    
    with open('userCollection/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    name = time.time()
    data[name] = maps

    with open('userCollection/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


@app.get('/', response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html",{'request':request})



@app.post("/upload")
async def upload(item: Item):
    if len(item.article) == 0 or len(item.content) == 0:
        return {'status': 'danger', 'details': "有些欄位尚未填寫"}
    maps = {"單位": '', "標題": item.article, "作者": '', "發布日": 0, "摘要": '', '全文': item.content}
    write_json(maps)
    return {'status': 'success', 'details': "上傳成功"}

@app.post("/pdf")
async def pdf(file: UploadFile = File(...)):
    contents = await file.read()
    data = api(contents)
    return {'status': 'success', 'data': data}


if __name__ == '__main__':
    api = pdfAPI()
    uvicorn.run(app, host="0.0.0.0",port=11143)