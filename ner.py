
import re
from .tokenizer import tokenize

PERSONS = [
    "alisher", "navoiy", "babur", "ulug'bek",
    "islom", "karimov", "shavkat", "mirziyoyev",
    "timur", "muhammad", "abdulla", "kamol"
]

LOCATIONS = [
    "toshkent", "samarqand", "buxoro", "xiva",
    "namangan", "andijon", "farg'ona", "qarshi",
    "termiz", "nukus", "o'zbekiston"
]

ORGANIZATIONS = [
    "university", "davlat", "vazirlik", "bank",
    "kompaniya", "institut", "akademiya",
    "maktab", "shifoxona", "bepro"
]

DATE_PATTERNS = [
    r'\d{4}-\d{2}-\d{2}',
    r'\d{1,2}\.\d{1,2}\.\d{4}',
    r'\d{4}',
]

def recognize_entities(text):
    entities = []
    text_lower = text.lower()

    for person in PERSONS:
        for match in re.finditer(person, text_lower):
            entities.append({"text": text[match.start():match.end()], "label": "SHAXS", "start": match.start()})

    for location in LOCATIONS:
        for match in re.finditer(location, text_lower):
            entities.append({"text": text[match.start():match.end()], "label": "JOY", "start": match.start()})

    for org in ORGANIZATIONS:
        for match in re.finditer(org, text_lower):
            entities.append({"text": text[match.start():match.end()], "label": "TASHKILOT", "start": match.start()})

    for pattern in DATE_PATTERNS:
        for match in re.finditer(pattern, text):
            entities.append({"text": match.group(), "label": "SANA", "start": match.start()})

    seen = set()
    result = []
    for e in entities:
        key = (e["text"].lower(), e["label"])
        if key not in seen:
            seen.add(key)
            result.append(e)

    return sorted(result, key=lambda x: x["start"])
