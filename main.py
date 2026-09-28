from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional
import uvicorn
import os
import socket

app = FastAPI()
DB = os.getenv("DB")
VERSION = os.getenv("VERSION", "1.0.0")

class HealthCheck(BaseModel):
    status: str = "OK"

class InfoResponse(BaseModel):
    version: str
    db: Optional[str] = None
    hostname: str


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")

@app.get(
    "/info",
    tags=["info"],
    summary="Get the application info",
    response_description="Return the application info",
    status_code=status.HTTP_200_OK,
    response_model=InfoResponse,
)
def get_version() -> dict:
    return {
        "version": os.getenv("VERSION", VERSION),
        "db": os.getenv("DB", DB),
        "hostname": os.getenv("HOSTNAME") or socket.gethostname(),
    }

def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


if __name__ == "__main__":
    main()