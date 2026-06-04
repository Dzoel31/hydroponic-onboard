from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.hydroponic import router as hydroponic_router
from utils.deps import get_session
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
app = FastAPI(
    title="Hydroponic Demo API",
    description="Demo backend sederhana untuk data hidroponik dengan endpoint GET dan POST.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hydroponic_router)

@app.get("/db-test")
async def db_test(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text("SELECT 1"))
    return {"result": result.scalar()}

