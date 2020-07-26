import csv
from typing import List, Union, Dict, IO

from fuzzywuzzy import fuzz

from app.business_layers.domain import Work
from app.business_layers.repository import WorkRepository


def process_csv(file: Union[IO, str, List[str]]):
    if isinstance(file, str):
        file = file.splitlines()
    return csv.DictReader(file, delimiter=",", quotechar="|")


async def update_existing_work(
    works_repo: WorkRepository, inserting_work: Work, existing_work: Work
) -> Work:
    if not existing_work.iswc and inserting_work.iswc:
        existing_work.iswc = inserting_work.iswc
        await works_repo.update(
            {"title": existing_work.title}, {"iswc": inserting_work.iswc}
        )

    modified = False
    for contributor in inserting_work.contributors:
        for existing_contributor in existing_work.contributors:
            if (
                fuzz.partial_token_sort_ratio(contributor, existing_contributor)
                > 80  # Compare names
            ):
                if len(contributor) > len(existing_contributor):
                    modified = True
                    existing_work.contributors[
                        existing_work.contributors.index(existing_contributor)
                    ] = contributor

                break
        else:
            # contributor not in existing work
            modified = True
            existing_work.contributors.append(contributor)

    if modified:
        await works_repo.update(
            {"title": existing_work.title}
            if not (existing_work.iswc or inserting_work.iswc)
            else {"iswc": inserting_work.iswc or existing_work.iswc},
            {"contributors": existing_work.contributors},
        )
    return existing_work


async def insert_work_use_case(works_repo: WorkRepository, work: Dict) -> Work:

    clean_work = {
        "title": work.get("title", "").strip(),
        "contributors": contributors
        if isinstance((contributors := work.get("contributors", [])), list)
        else contributors.split("|"),
        "iswc": work.get("iswc") or None,
        "source": work.get("source") or None,
        "id": int(ident)
        if (ident := work.get("id", "").isdigit()) or isinstance(ident, int)
        else None,
    }
    inserting_work = Work.from_dict(clean_work)

    existing_work = await works_repo.first(
        {"iswc": inserting_work.iswc}
    ) or await works_repo.first({"title": inserting_work.title})

    if not existing_work:
        return await works_repo.create(inserting_work.to_dict())

    return await update_existing_work(works_repo, inserting_work, existing_work,)


async def bulk_upload_works_use_case(
    works_repo: WorkRepository, works: List[Dict],
) -> List[Work]:
    return [await insert_work_use_case(works_repo, work) for work in works]


async def list_works_use_case(work_repo: WorkRepository,) -> List[Work]:
    return await work_repo.get_works()


async def get_work_use_case(
    work_repo: WorkRepository, work_isc: str
) -> Union[Work, None]:
    return await work_repo.first({"iswc": work_isc})
