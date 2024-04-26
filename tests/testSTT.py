import io
import sys
import unittest
from unittest.mock import patch, Mock
import speech_to_text
from .const import STT_RETURN

class TestSpeechToText(unittest.TestCase):
    def setUp(self):
        # Set up any resources needed by the test case
        pass
        
    def tearDown(self):
        # Clean up any resources used by the test case
        pass

    @patch('speech_recognition.Recognizer.recognize_google', return_value="hello world")
    @patch('speech_recognition.Recognizer.listen', return_value="mock_audio_data")
    def test_method_record_text(self, mock_listen, mock_recognize_google):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        text = speech_to_text.record_text()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), STT_RETURN)
        self.assertEqual(text, "hello world")

if __name__ == '__main__':
    unittest.main()
    