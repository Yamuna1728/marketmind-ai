from fastapi import APIRouter

router = APIRouter(
    prefix="/design",
    tags=["Design"]
)

@router.post("/")
async def generate_design():

    return {
        "message":
        "HuggingFace design generation endpoint"
    }