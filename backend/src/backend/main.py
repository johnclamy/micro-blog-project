from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.v1.router import api_router


app = FastAPI(title='Blog Post API', version='0.1.0')


# Allow CORS requests from Vite frontend during local development
origins = ["http://localhost:5173", "http://127.0.0.1:5173"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API v1 with a global prefix
app.include_router(api_router, prefix="/api/v1")