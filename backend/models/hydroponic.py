from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import UUID, DOUBLE_PRECISION
from config.db import Base
from uuid import UUID as PythonUUID, uuid7

class Hydroponic(Base):
    __tablename__ = 'hydroponic'

    id: Mapped[PythonUUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid7
    )
    moisture: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    temperature: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=False, default=0.0)
    humidity: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=False, default=0.0)
    ph: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=False, default=0.0)
    ec: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=False, default=0.0)
