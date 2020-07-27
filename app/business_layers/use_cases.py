from typing import List, Union, Dict

from app.business_layers.domain import Work
from app.business_layers.repository import WorkRepository
from app.utils.exceptions import MergeException
from app.utils.string_manipulation import build_best_string, is_similar


def merge_titles(existing_work: Work, inserting_work: Work) -> Union[str, None]:
    """
        Merge two titles into the best possible option
        :return: string if best is changed from existing else None
    """
    if existing_work.title == inserting_work.title:
        best_title = None
    elif not existing_work.title and inserting_work.title:
        best_title = inserting_work.title
    elif existing_work.title and not inserting_work.title:
        best_title = None
    else:
        try:
            best_title = build_best_string(existing_work.title, inserting_work.title)
        except MergeException:
            best_title = None
        else:
            if best_title == existing_work.title:
                best_title = None
    return best_title


def reconcile_contributors(existing_work: Work, inserting_work: Work) -> bool:
    """Insert contributors to existing work if new work has extra data"""
    modified = False
    for contributor in inserting_work.contributors:
        for existing_contributor in existing_work.contributors:
            if is_similar(contributor, existing_contributor):
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
    return modified


async def update_existing_work(
    works_repo: WorkRepository, inserting_work: Work, existing_work: Work
) -> Work:
    if not existing_work.iswc and inserting_work.iswc:
        existing_work.iswc = inserting_work.iswc
        await works_repo.update(
            {"title": existing_work.title}, {"iswc": inserting_work.iswc}
        )

    if reconcile_contributors(existing_work, inserting_work):
        await works_repo.update(
            {"title": existing_work.title}
            if not (existing_work.iswc or inserting_work.iswc)
            else {"iswc": inserting_work.iswc or existing_work.iswc},
            {"contributors": existing_work.contributors},
        )
    if best_title := merge_titles(existing_work, inserting_work):
        await works_repo.update(
            {"title": existing_work.title}
            if not (existing_work.iswc or inserting_work.iswc)
            else {"iswc": inserting_work.iswc or existing_work.iswc},
            {"title": best_title},
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
    }  # FIXME id is always 1
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
    parsed_works = {}
    for work in works:
        parsed_work = await insert_work_use_case(works_repo, work)
        parsed_works[parsed_work.iswc] = parsed_work
    return [work for iswc, work in parsed_works.items() if iswc]


async def list_works_use_case(work_repo: WorkRepository,) -> List[Work]:
    return await work_repo.get_works()


async def get_work_use_case(
    work_repo: WorkRepository, work_isc: str
) -> Union[Work, None]:
    return await work_repo.first({"iswc": work_isc})
