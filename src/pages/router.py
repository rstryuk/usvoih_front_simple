from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from http3 import AsyncClient, URL
from config import BACKEND_URL
import logging

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)


templates = Jinja2Templates(directory='templates')


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {'request': request})


@router.get("/listing")
async def get_base_page(request: Request):
    url: URL = f'{BACKEND_URL}/api/v1/lot/lots?limit=10&offset=0'
    client = AsyncClient()
    try:
        r = await client.get(url)
        lots = r.json()
        print(lots)
        return templates.TemplateResponse("listing.html", {'request': request, 'lots': lots})
    except Exception as e:
        print(e)
        lots = []
        return templates.TemplateResponse("listing.html", {'request': request})
