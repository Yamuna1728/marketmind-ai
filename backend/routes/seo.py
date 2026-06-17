from fastapi import APIRouter
from services.gemini_service import generate_content

router = APIRouter(prefix="/seo", tags=["SEO"])

@router.post("/")
async def analyze_seo(data: dict):

    result = generate_content(
        f"Analyze SEO for: {data}"
    )

    return {"seo_report": result}