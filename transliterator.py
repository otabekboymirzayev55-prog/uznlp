
LATIN_TO_CYRILLIC = {
    "ch": "ч", "sh": "ш", "ng": "нг",
    "gh": "ғ", "o'": "ў", "g'": "ғ",
    "a": "а", "b": "б", "d": "д",
    "e": "е", "f": "ф", "g": "г",
    "h": "ҳ", "i": "и", "j": "ж",
    "k": "к", "l": "л", "m": "м",
    "n": "н", "o": "о", "p": "п",
    "q": "қ", "r": "р", "s": "с",
    "t": "т", "u": "у", "v": "в",
    "x": "х", "y": "й", "z": "з",
    "A": "А", "B": "Б", "D": "Д",
    "E": "Е", "F": "Ф", "G": "Г",
    "H": "Ҳ", "I": "И", "J": "Ж",
    "K": "К", "L": "Л", "M": "М",
    "N": "Н", "O": "О", "P": "П",
    "Q": "Қ", "R": "Р", "S": "С",
    "T": "Т", "U": "У", "V": "В",
    "X": "Х", "Y": "Й", "Z": "З",
    "Ch": "Ч", "Sh": "Ш", "Gh": "Ғ",
}

CYRILLIC_TO_LATIN = {
    "а": "a", "б": "b", "д": "d",
    "е": "e", "ф": "f", "г": "g",
    "ҳ": "h", "и": "i", "ж": "j",
    "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p",
    "қ": "q", "р": "r", "с": "s",
    "т": "t", "у": "u", "в": "v",
    "х": "x", "й": "y", "з": "z",
    "ч": "ch", "ш": "sh", "ғ": "g'",
    "ў": "o'", "ъ": "'", "ё": "yo",
    "ю": "yu", "я": "ya", "э": "e",
    "А": "A", "Б": "B", "Д": "D",
    "Е": "E", "Ф": "F", "Г": "G",
    "Ҳ": "H", "И": "I", "Ж": "J",
    "К": "K", "Л": "L", "М": "M",
    "Н": "N", "О": "O", "П": "P",
    "Қ": "Q", "Р": "R", "С": "S",
    "Т": "T", "У": "U", "В": "V",
    "Х": "X", "Й": "Y", "З": "Z",
    "Ч": "Ch", "Ш": "Sh", "Ғ": "G'",
    "Ў": "O'",
}

def latin_to_cyrillic(text):
    result = ""
    i = 0
    while i < len(text):
        two_chars = text[i:i+2]
        if two_chars in LATIN_TO_CYRILLIC:
            result += LATIN_TO_CYRILLIC[two_chars]
            i += 2
        elif text[i] in LATIN_TO_CYRILLIC:
            result += LATIN_TO_CYRILLIC[text[i]]
            i += 1
        else:
            result += text[i]
            i += 1
    return result

def cyrillic_to_latin(text):
    result = ""
    for char in text:
        result += CYRILLIC_TO_LATIN.get(char, char)
    return result

def transliterate(text, direction="auto"):
    if direction == "auto":
        cyrillic_count = sum(1 for c in text if 'а' <= c <= 'я' or c in "ўқғҳ")
        latin_count = sum(1 for c in text if 'a' <= c <= 'z')
        direction = "cyrillic" if cyrillic_count > latin_count else "latin"
    if direction == "latin":
        return latin_to_cyrillic(text)
    else:
        return cyrillic_to_latin(text)
