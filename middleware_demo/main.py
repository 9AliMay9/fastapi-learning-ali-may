from fastapi import FastAPI
from middleware_demo.middleware import log_time_and_auth
from middleware_demo.routers import ping

app = FastAPI()

app.middleware("http")(log_time_and_auth)

app.include_router(ping.router)
