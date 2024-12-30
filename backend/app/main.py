from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import candidates
from app.config import settings

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication headers
    allow_methods=settings.cors_methods,  # Allowed HTTP methods
    allow_headers=settings.cors_allow_headers,  # Allowed headers
)

# Include the candidates router
app.include_router(candidates.router, prefix="/api", tags=["candidates"])
