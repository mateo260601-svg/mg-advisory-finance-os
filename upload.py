from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.config import LICENSE_KEY


router = APIRouter(prefix="/api/auth", tags=["auth"])


class LoginRequest(BaseModel):
    license_key: str


@router.post("/login")
def login(payload: LoginRequest):
    if payload.license_key.strip() != LICENSE_KEY:
        raise HTTPException(status_code=401, detail="Invalid license key")
    return {"ok": True, "token": "local-demo-token", "license": "valid"}

