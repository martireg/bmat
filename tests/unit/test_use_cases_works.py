from unittest import IsolatedAsyncioTestCase

from app.business_layers import use_cases
from app.business_layers.domain import Work
from tests.fixtures.dictionary_collection import test_work, test_work_csv


class MockRepo:
    async def get_works(self):
        return [Work.from_dict(test_work)]

    async def create_many(self, works):
        return [Work.from_dict(work) for work in works]

    async def first(self, filters):
        for key, filter in filters.items():
            if test_work.get(key) != filter:
                return None
        return Work.from_dict(test_work)


class TestWorkUseCases(IsolatedAsyncioTestCase):
    async def test_bulk_upload_works_use_case(self):
        works = await use_cases.bulk_upload_works_use_case(MockRepo(), test_work_csv)
        self.assertTrue(works[0])

    async def test_list_works_use_case(self):
        works = await use_cases.list_works_use_case(MockRepo(),)
        self.assertEqual(
            test_work.get("iswc"), works[0].iswc,
        )

    async def test_get_work_use_case(self):
        work = await use_cases.get_work_use_case(MockRepo(), test_work.get("iswc"),)
        self.assertEqual(work, Work.from_dict(test_work))
