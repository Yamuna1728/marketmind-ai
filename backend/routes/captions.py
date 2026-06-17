from fastapi import APIRouter
from services.gemini_service import generate_content

router = APIRouter(prefix="/captions", tags=["Captions"])

@router.post("/")
async def generate_caption(data: dict):

    prompt = f"""
    Generate social media captions:
    {data}
    """

    result = generate_content(prompt)

    return {"caption": result}