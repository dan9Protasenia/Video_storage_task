from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/app/templates/templates")


async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


async def health(request: Request):
    return templates.TemplateResponse("health.html", {"request": request})
