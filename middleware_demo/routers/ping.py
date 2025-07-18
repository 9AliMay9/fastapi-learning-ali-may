from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/ping")
async def ping(request: Request):
    return {
            "message": "pong",
            "user_id": request.state.user_id
    }
