import importlib.util
from pathlib import Path
import sys
import unittest

spec = importlib.util.spec_from_file_location('uznlp', Path(__file__).with_name('__init__.py'), submodule_search_locations=[str(Path(__file__).parent)])
uznlp = importlib.util.module_from_spec(spec)
sys.modules['uznlp'] = uznlp
spec.loader.exec_module(uznlp)

class LanguageTests(unittest.TestCase):
    def test_unicode_apostrophes_and_uppercase(self):
        self.assertEqual(uznlp.latin_to_cyrillic('O‘zbekiston'), 'Ўзбекистон')
        self.assertEqual(uznlp.transliterate('ЎЗБЕКИСТОН'), "O'ZBEKISTON")
        with self.assertRaises(ValueError): uznlp.transliterate('test', 'unknown')
    def test_tokens_and_entities(self):
        self.assertEqual(uznlp.tokenize('Salom!'), ['Salom','!'])
        self.assertFalse(any(e['label'] == 'TASHKILOT' for e in uznlp.recognize_entities('banknot')))
        self.assertEqual(len([e for e in uznlp.recognize_entities('Alisher va Alisher') if e['label'] == 'SHAXS']), 2)

if __name__ == '__main__': unittest.main()
