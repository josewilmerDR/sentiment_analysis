from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Define 3 unit tests in the said function and check for the validity of the following statement - label pairs.
        # “I love working with Python”: “SENT_POSITIVE”
        # “I hate working with Pyhton”: “SENT_NEGATIVE”
        # “I am neutral on Python”: “SENT_NEUTRAL”
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

#Call the unit tests.
unittest.main()