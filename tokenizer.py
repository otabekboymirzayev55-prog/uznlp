
import re

def tokenize(text):
    text = re.sub(r'([.,!?;:»«"()])', r' \1 ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = text.split(' ')
    return [t for t in tokens if t]

def tokenize_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]
