import unittest
from unittest.mock import Mock
from speech_to_text import record_text
from const import STT_RETURN

class TestSpeechToText(unittest.TestCase):
    def setUp(self):
        # Set up any resources used by the test case
        self.mock_speech_recognition = Mock()
        self.mock_speech_recognition.listen.return_value = "hello world"
        
    def tearDown(self):
        # Clean up any resources used by the test case
        pass

    def test_method_record_text(self):
        # Test if the recorded text matches the expected return value
        self.assertEqual(record_text(), STT_RETURN)

if __name__ == '__main__':
    unittest.main()