from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas.hydroponic import HydroponicCreate, HydroponicRead, HydroponicListResponse
from models import Hydroponic

class HydroponicStore:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def create(self, payload: HydroponicCreate) -> HydroponicRead:
        new_item = Hydroponic(**payload.model_dump())
        self.session.add(new_item)
        await self.session.commit()
        await self.session.refresh(new_item)
        return HydroponicRead.model_validate(new_item)

        # If using Raw SQL, you can do something like this:
        # query = text("""
        #     INSERT INTO hydroponics (moisture, temperature, humidity, ph,
        #     ec) VALUES (:moisture, :temperature, :humidity, :ph, :ec)
        #     RETURNING *
        # """)
        # result = await self.session.execute(query, payload.model_dump())
        # await self.session.commit()
        # return HydroponicRead(**result.mappings().first())

    async def retrieve(self) -> HydroponicListResponse:
        stmt = select(Hydroponic)
        result = await self.session.execute(stmt)
        items = result.scalars().all()

        return HydroponicListResponse(
            data=[HydroponicRead.model_validate(item) for item in items],
            total=len(items),
        )
