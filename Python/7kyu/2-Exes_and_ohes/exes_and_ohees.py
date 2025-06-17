from collections import Counter

def xo(s):
    char_count = Counter(s.lower())
    return char_count["x"] == char_count["o"]
