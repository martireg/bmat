import unicodedata

from fuzzywuzzy import fuzz

from app.config import SIMILARITY_THRESHOLD
from app.utils.exceptions import MergeException


def normalize_string(string: str) -> str:
    return (
        unicodedata.normalize("NFKD", string).encode("ASCII", "ignore").decode().lower()
    )


def punctuate_character(char: str) -> int:
    """Create a punctuation based on special characters and upper letters"""
    punctuation = 0
    if not unicodedata.is_normalized("NFKD", char):
        punctuation += 30
    if char.isupper():
        punctuation += 10
    return punctuation


def evaluate_string_richness(string: str) -> int:
    return sum(punctuate_character(char) for char in string)


def build_best_string(existing_string: str, inserting_string: str) -> str:
    """
    Build best string comparing tokens
    :raise: MergeException if strings have same token number but one or more are different
    """
    inserting_string_split = inserting_string.split()
    existing_string_split = existing_string.split()
    existing_token_number = len(existing_string_split)
    inserting_token_number = len(inserting_string_split)

    if existing_token_number != inserting_token_number:
        return (
            existing_string
            if existing_token_number > inserting_token_number
            else inserting_string
        )

    best_string_tokens = []
    for existing, inserting in zip(existing_string_split, inserting_string_split):
        if normalize_string(existing) != normalize_string(inserting):
            raise MergeException("Tokens do not match")
        elif existing == inserting:
            best_string_tokens.append(existing)
        else:
            best_string_tokens.append(
                existing
                if evaluate_string_richness(existing)
                >= evaluate_string_richness(inserting)
                else inserting
            )
    return " ".join(best_string_tokens)


def is_similar(string1: str, string2: str, threshold: int = None) -> bool:
    """Check if strings are similar"""
    if threshold is None:
        threshold = SIMILARITY_THRESHOLD
    return fuzz.partial_token_sort_ratio(string1, string2) >= threshold
