import aioredis

import uvicorn
from fastapi import FastAPI

from fastapi_limiter import FastAPILimiter

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

@app.on_event("startup") #fazla gelen api isteklerini sınırlandırmak için oluşturuldu.
async def startup():
    redis = await aioredis.create_redis_pool('redis://localhost:6379/0')
    FastAPILimiter.init(redis)

