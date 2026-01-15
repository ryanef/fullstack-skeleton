from sqlalchemy import Column, func, MetaData, select, String, Table, Uuid
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload
import uuid
from datetime import datetime

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid7(), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    
class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid7(), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())