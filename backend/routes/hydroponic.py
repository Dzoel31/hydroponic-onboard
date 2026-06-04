from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.hydroponic import HydroponicCreate, HydroponicListResponse, HydroponicRead
from services.hydroponic_service import HydroponicStore
from utils.deps import get_db_session, get_session

router = APIRouter(prefix="/hydroponics", tags=["hydroponics"])


@router.get("", response_model=HydroponicListResponse)
async def list_hydroponic_data(session: AsyncSession = Depends(get_session)) -> HydroponicListResponse | None:
    service = HydroponicStore(session)
    data = await service.retrieve()
    if data is None:
        return HydroponicListResponse(data=[], total=0)
    return data

@router.post("", response_model=HydroponicRead, status_code=status.HTTP_201_CREATED)
async def create_hydroponic_data(payload: HydroponicCreate, session: AsyncSession = Depends(get_session)) -> HydroponicRead:
    service = HydroponicStore(session)
    return await service.create(payload)