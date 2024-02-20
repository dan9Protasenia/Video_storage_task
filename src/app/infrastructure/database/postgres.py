from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.app.core.handlers.errors import InternalServerError
from src.app.infrastructure.database.config_loader import DATABASE_URL

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def get_db():
    """
        Database dependency for FastAPI routes.

        This is an asynchronous generator that yields a SQLAlchemy session wrapped in a transaction.

        """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()

        except Exception as e:
            await session.rollback()

            raise InternalServerError(str(e))
