def get_num_words(text):
    """
    Return the number of words in the given text.
    Splits on any whitespace.
    """
    return len(text.split())

def sort_char_counts(char_counts):
    """
    Given a dict {char: count}, return a list of dicts
    sorted descending by count.  
    Each element looks like {"char": <letter>, "num": <count>}.
    """
    # 1) Turn the dict into a list of small dicts
    items = [{"char": c, "num": n} for c, n in char_counts.items()]
    # 2) Sort in-place from largest to smallest
    items.sort(reverse=True, key=lambda d: d["num"])
    return items
