import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi import APIRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

router = APIRouter()
app = FastAPI()

# Include Django's ASGI application
app.mount('/v1', get_asgi_application())
@router.get('/hello')
def hello_world():
    return {'message': 'Hello from Django + FastAPI!'}

#app = FastAPI()
app.include_router(router, prefix='/v2')
