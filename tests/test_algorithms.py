import unittest

from phonetisch import soundex, caverphone

class TestSoundex(unittest.TestCase):

    def test_encode(self):
        assert soundex.encode_word("Example") == soundex.encode_word("Ekzampul")



class TestCaverphone(unittest.TestCase):
    def test_encode(self):
        assert caverphone.encode_word("Lee") == caverphone.encode_word("L11111")
        assert caverphone.encode_word("Thompson") == caverphone.encode_word("TMPSN1")