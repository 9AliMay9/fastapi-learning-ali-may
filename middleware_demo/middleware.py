import time
from fastapi import Request
from fastapi.responses import JSONResponse

async def log_time_and_auth(request: Request, call_next):
    if request.url.path.startswith("/docs") or request.url.path in ("/openapi.json", "/redoc"):
        return await call_next(request)

    token = request.headers.get("x-token")
    if token != "secret-token":
        return JSONResponse(status_code=401, content={"detail": "Invalid Token"})

    request.state.user_id = "user-123"
    response = await call_next(request)
    
    return response
