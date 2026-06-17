from fastapi import APIRouter
from services.trend_service import get_trends

router = APIRouter(prefix="/trends", tags=["Trends"])

@router.get("/{keyword}")
async def trends(keyword: str):

    return {
        "trends": get_trends(keyword)
    }