from fastapi import FastAPI, status
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()
DB = os.getenv("DB")
VERSION = os.getenv("VERSION", "1.0.0")

class HealthCheck(BaseModel):
    status: str = "OK"


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
)
def get_version() -> dict:
    return {"version": VERSION, "db": DB}

def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


if __name__ == "__main__":
    main()