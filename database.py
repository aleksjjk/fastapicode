from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,sessionmaker
engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


# table
class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str | None]]


# create table
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


# delete tables
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
