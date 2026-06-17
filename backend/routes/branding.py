from fastapi import APIRouter
from services.gemini_service import generate_content

router = APIRouter(
    prefix="/branding",
    tags=["Branding"]
)


@router.post("/")
async def generate_brand(data: dict):

    prompt = f"""
    Generate complete branding:
    {data}
    """

    result = generate_content(prompt)

    return {
        "tagline": "AI Generated Tagline",
        "mission": result,
        "voice": "Professional",
        "audience": "Startups and SMEs",
        "colors": [
            "#7C3AED",
            "#2563EB",
            "#F8FAFC"
        ]
    }