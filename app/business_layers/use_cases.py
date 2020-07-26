from typing import List, Union

from app.business_layers.domain import Work
from app.business_layers.repository import WorkRepository


async def bulk_upload_works_use_case(
    works_repo: WorkRepository, csv_works: str,
) -> List[Work]:
    """Upload csv into database"""
    pass


async def list_works_use_case(work_repo: WorkRepository,) -> List[Work]:
    return await work_repo.get_works()


async def get_work_use_case(
    work_repo: WorkRepository, work_isc: str
) -> Union[Work, None]:
    return await work_repo.first({"iswc": work_isc})
