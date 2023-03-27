from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from http3 import AsyncClient, URL

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
    url: URL = 'http://127.0.0.1:8000/api/v1/lot/lots?limit=10&offset=0'
    client = AsyncClient()
    r = await client.get(url)
    lots = r.json()
    return templates.TemplateResponse("listing.html", {'request': request, 'lots': lots})
