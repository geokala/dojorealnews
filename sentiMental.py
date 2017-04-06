#! /usr/bin/env python
from textblob import TextBlob
import sys

def get_sentiment(text):
    text = TextBlob(text)
    return text.sentiment[0]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {prog} <text to analyse>'.format(prog=sys.argv[0]))
        sys.exit(1)

    print(get_sentiment(sys.argv[1]))
