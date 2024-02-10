from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/app/templates/templates")


@router.get("/health", response_model=dict)
async def health_check(request: Request):
    return templates.TemplateResponse("health.html", {"request": request})


@router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
