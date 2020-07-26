from unittest import TestCase

from app.business_layers.domain import Work
from tests.fixtures.dictionary_collection import test_work, expected_work


class TestWorkDomain(TestCase):
    def test_work_init(self):
        work = Work(**test_work)

        self.assertEqual(work.to_dict(), expected_work)

    def test_work_from_dict(self):
        work = Work.from_dict(test_work)
        self.assertAlmostEqual(work.to_dict().get("iswc"), expected_work.get("iswc"))

    def test_work_to_dict(self):
        work = Work.from_dict(test_work)
        self.assertEqual(work.to_dict(), expected_work)

    def test_equality(self):
        work1 = Work.from_dict(test_work)
        work2 = Work.from_dict(test_work)
        self.assertEqual(work1, work2)
        self.assertEqual(work1, test_work)
        self.assertEqual(test_work, work1)
        self.assertTrue(work1 in [test_work])
