from fastapi import APIRouter
from .asgi import app
router = APIRouter()

@router.get('/hello')
def hello_world():
    return {'message': 'Hello from Django + FastAPI!'}

#app = FastAPI()
app.include_router(router, prefix='/api')
