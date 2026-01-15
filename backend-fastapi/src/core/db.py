from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey, func, select
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload
from .settings import PG_URL
from src.models.db_models import Base, Account, User

engine = create_async_engine(PG_URL, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
