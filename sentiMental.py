#! /usr/bin/env python
from textblob import TextBlob
import sys

def get_sentiment(text):
    text = TextBlob(text)
    return text.sentiment[0]

def get_title(text):
    text = TextBlob(text)
    return text.tokens[0]

def get_categories(text):
    text = TextBlob(text)
    phrases = text.noun_phrases
    if len(phrases) >= 2:
        cat1 = phrases[0]
        cat2 = phrases[1]
    elif len(phrases) == 1:
        cat1 = phrases[0]
        cat2 = 'correct'
    else:
        cat1 = 'peroni'
        cat2 = 'nastro azzurro'
    return cat1, cat2

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {prog} <text to analyse>'.format(prog=sys.argv[0]))
        sys.exit(1)

    print(get_sentiment(sys.argv[1]))
    print(get_title(sys.argv[1]))
    print(get_categories(sys.argv[1]))
