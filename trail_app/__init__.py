from fastapi import FastAPI, Depends
from trail_app import config


def create_app() -> FastAPI:

    # TO-DO: initialize db
    app = FastAPI()

    from trail_app.trail_api import trails_router
    app.include_router(trails_router)

    @app.get("/")
    async def root():
        return {"message": "Hurroh wuwold"}

    return app
