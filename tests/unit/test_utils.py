from unittest import TestCase

from tests.fixtures.dictionary_collection import test_work_csv
from app.utils import string_manipulation


class TestUtils(TestCase):

    def test_string_similarity(self):
        self.assertTrue(string_manipulation.is_similar(
            "Martí Regola i Macias",
            "Martí R.",
            threshold=80
        ))
        self.assertFalse(string_manipulation.is_similar(
            "Martí Regola i Macias",
            "Alba Santaló Bardera",
            threshold=80
        ))

    def test_string_merge(self):
        self.assertEqual(
            string_manipulation.build_best_string("Marti Regola macias", "Martí regola macias"),
            "Martí Regola macias"
        )
        self.assertEqual(
            string_manipulation.build_best_string("me enamore", "me enamoré"),
            "me enamoré"
        )
        self.assertEqual(
            string_manipulation.build_best_string("enamore", "me enamore"),
            "me enamore"
        )
        self.assertEqual(
            string_manipulation.build_best_string("me enamore", "enamore"),
            "me enamore"
        )
