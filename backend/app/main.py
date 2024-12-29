from fastapi import FastAPI
from .routes import candidates

app = FastAPI()

# Include the candidates router
app.include_router(candidates.router, prefix="/api", tags=["candidates"])
