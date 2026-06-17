from fastapi import APIRouter

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/")
async def analytics():

    return {
        "reach": 28600,
        "impressions": 78500,
        "clicks": 6800,
        "ctr": "8.7%"
    }