from fastapi import APIRouter

trails_router = APIRouter(
    prefix="/trails"
)


@trails_router.get("/start")
async def start_trails():
    return {"message": "starting on the trail"}

