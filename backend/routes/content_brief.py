from fastapi import APIRouter
from services.gemini_service import generate_content
import json

router = APIRouter(
    prefix="/content-brief",
    tags=["Content Brief"]
)

@router.post("/")
async def generate_brief(data: dict):

    prompt = f"""
Generate a marketing content brief.

Title:
{data.get("title")}

Description:
{data.get("description")}

Return JSON:

{{
  "goal":"",
  "hook":"",
  "talking_points":[],
  "cta":"",
  "visual":"",
  "hashtags":[]
}}
"""

    result = generate_content(prompt)

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)