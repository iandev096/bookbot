from sys import argv, exit
from stats import get_word_count, get_char_count, get_sorted_char_count


def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        file_content = f.read()
        return file_content


def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path = argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = get_sorted_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")

    print("============ END ============")


if __name__ == "__main__":
    main()
