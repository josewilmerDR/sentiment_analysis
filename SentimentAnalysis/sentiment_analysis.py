"""
Sentiment Analysis Module
This module provides a function to analyze sentiment using the Watson Embedded AI Libraries.
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Analyzes the sentiment of the given text.

    Parameters:
    text_to_analyse (str): The text to be analyzed.

    Returns:
    dict: A dictionary containing the sentiment label and score.
    """
    url = (
        'https://sn-watson-sentiment-bert.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)

    # Initialize variables
    label = None
    score = None

    # Validate the response of the server
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif formatted_response["documentSentiment"]["sentimentMentions"][0]["span"]["text"] == "":
        label = "NoText"
        score = None
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}
