from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class BaseTable(Base):
    """
    Abstract base class for all models, providing default ID and timestamp fields.

    Attributes:
        id (Integer): The primary key for the record, automatically indexed.
        created_at (DateTime): Timestamp of record creation, set to the current time by default.
        updated_at (DateTime): Timestamp of the last record update, set to the current time upon updating.
    """

    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
