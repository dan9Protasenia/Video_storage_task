from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/health", response_model=dict)
async def health_check():
    return {"status": "OK"}


@router.get("/home", response_class=HTMLResponse)
async def home():
    return "<html><body><h1>🦄</h1></body></html>"
