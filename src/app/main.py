from dotenv import load_dotenv

load_dotenv()

from src.app.config import MainConfig
from src.app.startup import create_app

config = MainConfig()
app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8001)
