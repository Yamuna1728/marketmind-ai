from unittest import result

from fastapi import APIRouter
from services.gemini_service import generate_content
import json

router = APIRouter(
    prefix="/calendar",
    tags=["Calendar"]
)

@router.post("/")
async def create_calendar(data: dict):

    prompt = f"""
You are a senior content strategist.

Generate a detailed 4-week content calendar.

Business Name:
{data.get("business")}

Industry:
{data.get("industry")}

Target Audience:
{data.get("audience")}

Marketing Goal:
{data.get("goal")}

Brand Description:
{data.get("brandDescription")}

Website URL:
{data.get("websiteUrl")}

Additional Information:
{data.get("additionalInfo")}

Requirements:

- Create 4 weeks
- Each week should contain 5-7 content ideas
- Include platform
- Include posting time
- Include content type
- Include goal
- Avoid repetitive content
- Include educational content
- Include engagement content
- Include authority-building content
- Include conversion-focused content
- Include trending industry angles where possible

Return ONLY valid JSON using this structure:

{{
  "summary": "...",
  "weeks": [
    {{
      "week": "Week 1",
      "days": [
        {{
          "day": "Monday",
          "title": "...",
          "description": "...",
          "platform": "...",
          "time": "...",
          "content_type": "...",
          "goal": "..."
        }}
      ]
    }}
  ]
}}

    Generate exactly 4 weeks.
    Generate Monday-Sunday for every week.
    No markdown.
    No explanation.
    JSON only.
    """

    
    print("Calendar request received")
    print(data)

    result = generate_content(prompt)

    print("Result received")

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:
        return json.loads(result)

    except Exception as e:
        print("JSON PARSE ERROR:")
        print(str(e))

        return {
        "summary": "Unable to parse response",
        "weeks": []
    }