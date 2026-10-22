from fastapi import HTTPException, Header

VALID_TOKEN = "ENSEA2026"

def secure (authorization: str = Header(None)):
    if authorization != f"Bearer {VALID_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized : Token invalide")
