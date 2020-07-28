from unittest import IsolatedAsyncioTestCase

from app.business_layers import use_cases
from app.business_layers.domain import Work
from app.utils.csv_manipulation import process_csv, create_csv
from tests.fixtures.dictionary_collection import test_work_csv


class MockRepo:
    def __init__(self):
        self.works = []

    async def get_works(self):
        return [Work.from_dict(work) for work in self.works]

    async def create_many(self, works):
        self.works.extend(works)
        return [Work.from_dict(work) for work in works]

    async def create(self, work):
        self.works.append(work)
        return Work.from_dict(work)

    async def first(self, filters):
        for work in self.works:
            for key, filter in filters.items():
                if work.get(key) != filter:
                    break
            else:
                return Work.from_dict(work)
        return None

    async def update(self, filters, update):
        for work in self.works:
            for key, filter in filters.items():
                if work.get(key) != filter:
                    break
            else:
                work.update(update)
                return Work.from_dict(work)
        return None


class TestWorkUseCases(IsolatedAsyncioTestCase):
    async def test_bulk_upload_works_use_case(self):

        repo = MockRepo()
        works = await use_cases.bulk_upload_works_use_case(
            repo, process_csv(test_work_csv)
        )
        self.assertEqual(len(works), 4)
        self.assertEqual(len(works[1].contributors), 4)
