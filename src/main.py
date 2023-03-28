from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from pages.router import router as front_router
app = FastAPI()

app.include_router(front_router)

origins = [
    'http://localhost:8000',
    'http://localhost:3000',
    'https://usvoih-front-simple.onrender.com'
]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['GET', 'POST', 'PATCH',
                                  'DELETE', 'PUT', 'OPTIONS'],
                   allow_headers=['*'])
