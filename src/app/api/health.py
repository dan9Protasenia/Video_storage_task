from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/app/templates/templates")


@router.get("/health", response_model=dict)
async def health_check(request: Request):
    return templates.TemplateResponse("health.html", {"request": request})
