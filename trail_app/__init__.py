from fastapi import FastAPI


def create_app() -> FastAPI:

    # TO-DO: initialize db
    app = FastAPI()

    from trail_app.trail_api import trails_router
    app.include_router(trails_router)

    @app.get("/")
    async def root():
        return {"message": "Hurroh wuwold"}

    return app
