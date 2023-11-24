import unittest
from datetime import datetime
from unittest.mock import patch

import requests

from join_words import join_words


def my_print(text, visible=True):
    if visible:
        print(text)


def mocked_get(*args,**kwargs):
    return "badger-racoon"

class TestJoinWords(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        my_print("\nA test suit begins")

    @classmethod
    def tearDownClass(cls):
        my_print("\nA test suit ends")

    def setUp(self):
        my_print("\nA test begins")

    def tearDown(self):
        my_print("\nA test ends")

    def test_smoke(self):
        my_print("Test #1")
        result = join_words("word1", "word2")

        self.assertEqual(result, "word1-word2")

    @unittest.skip("This is skip")
    def test_skip_test(self):
        my_print("skipped")
        pass

    @unittest.expectedFailure
    def test_xfail(self):
        my_print("expectedFailure")
        result = join_words(666, "word2")
        self.assertEqual(result, "word1-word2")

    @patch("requests.get", side_effect=mocked_get)
    def test_mock(self, mock):
        response = requests.get("https://www.google.com/search?q=badger")
        self.assertEqual(response, "badger-racoon")

    @unittest.skipIf(datetime.now().weekday() in [0, 2, 4],
                     "Skip on Monday, Wednesday, Friday")
    def test_skip_if_test(self):
        result = join_words("word1", "word2")
        self.assertEqual(result, "word1-word2")

    @patch('requests.get')
    def test_google_request(self, mock_get):
        mock_get.return_value.status_code = 404
        response = requests.get('https://www.google.com')

        self.assertEqual(response.status_code, 404)