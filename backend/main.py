from fastapi import FastAPI
from database.config import settings
app = FastAPI()


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    # include_router(app)
    # create_tables()
    return app
app = start_application()
@app.get("/")
def firstFunc():
    return "pradipta testing"