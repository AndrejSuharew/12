from fastapi import FastAPI, HTTPException, status

from app.config import settings
from app.database import check_db_connection

app = FastAPI(title=settings.app_name)


@app.get("/")
def root() -> dict[str, str]:
    return {"service": settings.app_name, "status": "running"}


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check() -> dict[str, str]:
    if not check_db_connection():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed",
        )
    return {"status": "ok", "database": "connected"}
