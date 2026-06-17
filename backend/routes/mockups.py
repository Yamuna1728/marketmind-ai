from fastapi import APIRouter

router = APIRouter(
    prefix="/mockups",
    tags=["Mockups"]
)

@router.post("/")
async def generate_mockup():

    return {
        "message":
        "Mockup generation endpoint"
    }