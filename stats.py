from typing import Union


def get_word_count(book_text: str) -> int:
    words = book_text.split()
    return len(words)


def get_char_count(book_text: str) -> dict[str, int]:
    char_count = {}

    for char in book_text:
        cur_char = char.lower().strip()
        if cur_char in char_count and cur_char.isalpha():
            char_count[cur_char] += 1
        else:
            char_count[cur_char] = 1

    return char_count


# {"char": "b", "count": 4868}
SortedCharCount = dict[str, Union[str, int]]


def get_sorted_char_count(char_count: dict[str, int]) -> list[SortedCharCount]:
    sorted_char_count = []
    for char, num in char_count.items():
        sorted_char_count.append({"char": char, "num": num})

    sorted_char_count.sort(key=lambda x: x["num"], reverse=True)
    return sorted_char_count
