from stats import get_num_words

def get_book_text(filepath):
    """
    Read the contents of the file at the given filepath and return as a string.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    # Path to the book file
    path = 'books/frankenstein.txt'

    # Read the book text
    book_text = get_book_text(path)

    # Use the refactored function to count words
    num_words = get_num_words(book_text)

    # Print the result
    print(f"{num_words} words found in the document")

if __name__ == '__main__':
    main()
