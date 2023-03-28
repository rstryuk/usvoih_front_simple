from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from http3 import AsyncClient, URL
from config import BACKEND_URL
import logging

router = APIRouter(
    prefix='',
    tags=['Pages']
)


templates = Jinja2Templates(directory='templates')


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {'request': request})


@router.get("/index")
async def get_base_page(request: Request):
    url: URL = f'{BACKEND_URL}/api/v1/lot/lots?limit=10&offset=0'
    client = AsyncClient()
    print(url)
    try:
        r = await client.get(url)
        lots = r.json()
        # print(lots)
        return templates.TemplateResponse("listing.html", {'request': request, 'lots': lots})
    except Exception as e:
        print(e)
        lots = []
        return templates.TemplateResponse("listing.html", {'request': request})


@router.get('/lot/{lot_id}')
async def display_lot(request: Request, lot_id):
    url: URL = f'{BACKEND_URL}/api/v1/lot/{lot_id}'

    client = AsyncClient()
    print(url)
    try:
        r = await client.get(url)
        lot = r.json()
        # print(lots)
        return templates.TemplateResponse("lot.html", {'request': request, 'lot': lot})
    except Exception as e:
        print(e)
        lots = {}
        return templates.TemplateResponse("lot.html", {'request': request})


@router.get('/login')
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {'request': request})
