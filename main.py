from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print('started polling')
    yield
    # Clean up the ML models and release the resources
    print('ended polling')


app = FastAPI(lifespan=lifespan)
app.include_router(router)
