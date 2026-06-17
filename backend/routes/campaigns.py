from fastapi import APIRouter
from services.gemini_service import generate_content

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])

@router.post("/")
async def generate_campaign(data: dict):

    prompt = f"""
    Create a marketing campaign:
    {data}
    """

    result = generate_content(prompt)

    return {"campaign": result}