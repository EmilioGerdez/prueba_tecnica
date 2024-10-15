"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
import os
from fastapi import FastAPI, APIRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialize FastAPI app
app = FastAPI()

# Mount Django's ASGI application to handle the root path
django_app = get_asgi_application()
app.mount("/v1", django_app)

# Create a router for FastAPI
router = APIRouter()

# Define FastAPI routes
@router.get("/hello")
async def hello_route():
    return {"message": "Hello from FastAPI"}

# Include the FastAPI router under the /v2 path
app.include_router(router, prefix="/v2")

# Define the ASGI application
application = app

