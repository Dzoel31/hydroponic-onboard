from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class HydroponicBase(BaseModel):
    moisture: int = Field(ge=0, le=100, description="Kelembapan media tanam dalam persen")
    temperature: float = Field(ge=0, description="Suhu air atau lingkungan dalam Celsius")
    humidity: float = Field(ge=0, le=100, description="Kelembapan udara dalam persen")
    ph: float = Field(ge=0, description="Nilai pH larutan")
    ec: float = Field(ge=0, description="Electrical conductivity larutan")


class HydroponicCreate(HydroponicBase):
    pass


class HydroponicRead(HydroponicBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)


class HydroponicListResponse(BaseModel):
    data: list[HydroponicRead]
    total: int