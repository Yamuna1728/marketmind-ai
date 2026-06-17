from fastapi import APIRouter
from services.gemini_service import generate_content

router = APIRouter(prefix="/ads", tags=["Ads"])

@router.post("/")
async def create_ad(data: dict):

    result = generate_content(
        f"Generate ad copy: {data}"
    )

    return {"ad": result}