
ALL_SUFFIXES = sorted([
    "lar", "ler",
    "ning", "gacha", "dan", "da", "ga", "ni",
    "imizdan", "imizga", "imizni", "imizda",
    "ingizdan", "ingizga", "ingizni",
    "imdan", "imga", "imni", "imda",
    "ingdan", "ingga", "ingni",
    "lariga", "larida", "laridan",
    "imiz", "ingiz", "lari",
    "im", "ing",
    "moqchiman", "moqchisiz", "moqchi",
    "yapman", "yapsiz", "yapti",
    "yabman", "yabsiz", "yabdi",
    "aman", "asiz", "adi",
    "dik", "dingiz", "di",
    "sin", "ish", "moq",
    "gan", "kan",
], key=len, reverse=True)

MIN_STEM_LENGTH = 3

def stem(word):
    word_lower = word.lower()
    for suffix in ALL_SUFFIXES:
        if word_lower.endswith(suffix):
            candidate = word_lower[:-len(suffix)]
            if len(candidate) >= MIN_STEM_LENGTH:
                return candidate
    return word_lower

def stem_tokens(tokens):
    return [stem(t) for t in tokens]
