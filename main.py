import sys 
from stats import get_num_words, sort_char_counts

def get_book_text(filepath):
    """
    Read the contents of the file at the given filepath and return as a string.
    """
    with open(filepath, 'r') as f:
        return f.read()


def main():
    # Path to the book file
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    # Read the book text as-is
    book_text = get_book_text(path)

    # Word count
    num_words = get_num_words(book_text)

    # Build character counts (alphabetical only)
    char_counts = {}
    for ch in book_text:
        if ch.isalpha():
            key = ch.lower()
            char_counts[key] = char_counts.get(key, 0) + 1

    # Sort characters by count descending
    sorted_chars = sort_char_counts(char_counts)

    # Print formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == '__main__':
    main()
