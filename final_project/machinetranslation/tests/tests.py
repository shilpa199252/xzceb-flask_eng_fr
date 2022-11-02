import unittest
from translator import english_tofrench, french_toenglish

class test_translation(unittest.TestCase):
    def test_english_tofrench(self):
        self. assertEqual(english_tofrench(""),"null input")
        self. assertEqual(english_tofrench("Hello"),"Bonjour")

class test_translation1(unittest.TestCase):
    def test_french_toenglish(self):
        self. assertEqual(french_toenglish(""),"null input")
        self. assertEqual(french_toenglish("Bonjour"),"Hello")

unittest.main()
    
        