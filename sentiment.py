
from .tokenizer import tokenize

POSITIVE_WORDS = [
    "yaxshi", "zo'r", "ajoyib", "mukammal",
    "mamnun", "baxtli", "yoqdi", "kuchli",
    "foydali", "qulay", "tez", "arzon",
    "sifatli", "tavsiya", "rahmat", "barakali",
    "ishonchli", "professional", "aqlli", "chiroyli"
]

NEGATIVE_WORDS = [
    "yomon", "dahshatli", "xato", "muammo",
    "qiyin", "sekin", "qimmat", "sifatsiz",
    "ishonchsiz", "yoqmadi", "noto'g'ri",
    "buzuq", "past", "shikoyat", "umidsiz"
]

INTENSIFIERS = {
    "juda": 1.5, "eng": 1.5,
    "ancha": 1.3, "biroz": 0.7, "sal": 0.7,
}

NEGATIONS = ["emas", "yo'q", "umuman", "hech"]

def analyze_sentiment(text):
    tokens = tokenize(text.lower())
    pos_score = 0
    neg_score = 0
    multiplier = 1.0
    negate = False

    for token in tokens:
        if token in INTENSIFIERS:
            multiplier = INTENSIFIERS[token]
            continue
        if token in NEGATIONS:
            negate = True
            continue
        if token in POSITIVE_WORDS:
            score = 1.0 * multiplier
            neg_score += score if negate else 0
            pos_score += 0 if negate else score
        elif token in NEGATIVE_WORDS:
            score = 1.0 * multiplier
            pos_score += score if negate else 0
            neg_score += 0 if negate else score
        multiplier = 1.0
        negate = False

    total = pos_score + neg_score
    if total == 0:
        return {"label": "neutral", "score": 0.5}

    pos_ratio = round(pos_score / total, 2)
    label = "positive" if pos_ratio > 0.6 else "negative" if pos_ratio < 0.4 else "neutral"
    return {"label": label, "score": pos_ratio}
