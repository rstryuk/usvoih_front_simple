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
        return templates.TemplateResponse("listing.html", {'request': request, 'lots': lots, 'backend': BACKEND_URL})
    except Exception as e:
        print(e)
        lots = []

        return templates.TemplateResponse("listing.html", {'request': request})


@ router.get('/lot/{lot_id}')
async def display_lot(request: Request, lot_id):
    url: URL = f'{BACKEND_URL}/api/v1/lot/{lot_id}'

    client = AsyncClient()
    print(url)
    try:
        r = await client.get(url)
        lot = r.json()
        return templates.TemplateResponse("lot.html", {'request': request, 'lot': lot, 'backend': BACKEND_URL})
    except Exception as e:
        print(e)
        lot = {}
        return templates.TemplateResponse("lot.html", {'request': request})


@ router.get('/login')
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {'request': request})


@router.get('/me')
async def profile_page(request: Request):
    # https://usvoih-front-simple.onrender.com/me
    # ?id=360344865&first_name=Roman&username=rstryuk&auth_date=1680067985
    # &hash=fda8771b596aab4a65c51a25df9961621385f15439bdf97b0edea29916adc7cf
    body = await request.body()
    params = request.query_params

    return templates.TemplateResponse('me.html', {'request': request, 'body': params})
