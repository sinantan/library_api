from fastapi import HTTPException

async def get_token(token: str):
    if token != "secret-token":
        raise HTTPException(status_code=400, detail="Token is not provided")