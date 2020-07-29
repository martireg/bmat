from unittest import TestCase

from app.utils import string_manipulation, csv_manipulation


class TestUtils(TestCase):
    def test_string_similarity(self):
        self.assertTrue(
            string_manipulation.is_similar(
                "Martí Regola i Macias", "Martí R.", threshold=80
            )
        )
        self.assertFalse(
            string_manipulation.is_similar(
                "Martí Regola i Macias", "Marti R.", threshold=99
            )
        )
        self.assertFalse(
            string_manipulation.is_similar(
                "Martí Regola i Macias", "Alba Santaló Bardera", threshold=80
            )
        )

    def test_string_merge(self):
        self.assertEqual(
            string_manipulation.build_best_string(
                "Marti Regola macias", "Martí regola macias"
            ),
            "Martí Regola macias",
        )
        self.assertEqual(
            string_manipulation.build_best_string("me enamore", "me enamoré"),
            "me enamoré",
        )
        self.assertEqual(
            string_manipulation.build_best_string("enamore", "me enamore"), "me enamore"
        )
        self.assertEqual(
            string_manipulation.build_best_string("me enamore", "enamore"), "me enamore"
        )

    def test_string_normalize(self):
        self.assertEqual(
            string_manipulation.normalize_string("me enamoré",), "me enamore"
        )

    def test_build_csv(self):
        self.assertEqual(
            [i for i in csv_manipulation.stream_csv_from_dicts([], [])], [b""]
        )

        csv = b"".join(
            csv_manipulation.stream_csv_from_dicts(
                [
                    {"header1": "key1", "header2": None},
                    {"header1": 3, "header2": ["key4", "key5"]},
                ],
                ["header1", "header2"],
            )
        )
        expected = """header1,header2
key1,
3,key4|key5""".encode()
        self.assertEqual(
            csv, expected,
        )
