from typing import AsyncGenerator
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker
from settings import settings

# Create declarative base
Base = declarative_base()

# Synchronous database engine and session
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    pool_recycle=300,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Asynchronous database engine and session
async_engine = create_async_engine(
    settings.database_url_async,
    pool_pre_ping=True,
    pool_recycle=300,
)

AsyncSessionLocal = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get asynchronous database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
