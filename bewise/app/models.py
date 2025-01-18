from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from bewise.app.config import settings

Base = declarative_base()

engine = create_async_engine(settings.db_url)

async_session = AsyncSession(engine)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


class Application(Base):
    __tablename__ = "application"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50))
    description = Column(String(50))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
