import os
from fastapi import FastAPI, APIRouter
from django.core.asgi import get_asgi_application
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Receive, Scope, Send

# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialize FastAPI app
fastapi_app = FastAPI()

# Mount Django's ASGI application
django_app = get_asgi_application()

# Create FastAPI router
router = APIRouter()

# Define FastAPI route
@router.get('/hello')
def hello_world():
    return {'message': 'Hello from Django + FastAPI!'}

# Include FastAPI router
fastapi_app.include_router(router, prefix='/v2')

class CustomASGIMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)
        self.django_app = django_app
        self.fastapi_app = fastapi_app

    async def dispatch(self, request, call_next):
        if request.url.path.startswith('/v2'):
            return await fastapi_app(request.scope, request.receive, request.send)
        else:
            return await django_app(request.scope, request.receive, request.send)

# Create the main ASGI app
app = CustomASGIMiddleware(django_app)
