
# UzNLP — O'zbek tili NLP kutubxonasi

O'zbek tili uchun tabiiy til ishlov berish kutubxonasi.

## Imkoniyatlar

- Transliteratsiya (Lotin ↔ Kirill)
- Tokenizatsiya
- Stemming
- Sentiment tahlil
- NER (nom, joy, tashkilot aniqlash)

## O‘rnatish

```sh
python -m pip install .
```

Bu qoida va lug‘atga asoslangan boshlang‘ich kutubxona; sentiment va NER natijalari ML modeli aniqligi sifatida talqin qilinmaydi.

## Ishlatish

```python
import uznlp

# Transliteratsiya
uznlp.transliterate("Salom dunyo")

# Tokenizatsiya
uznlp.tokenize("Men Toshkentda yashayman")

# Stemming
uznlp.stem("kitoblardan")

# Sentiment
uznlp.analyze_sentiment("Bu juda yaxshi!")

# NER
uznlp.recognize_entities("Alisher Navoiy Samarqandda tug'ilgan")
```

## Muallif

Otabek Boymirzayev — O'zbekiston
