import re
import string
from typing import List

import Stemmer

STOPWORDS = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
                 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
                 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'movie'])

PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))


def punctuation_filter(tokens):
    return [PUNCTUATION.sub('', token) for token in tokens]


stemmer = Stemmer.Stemmer("english")


def stem_words(tokens: List[str]) -> List[str]:
    return [stemmer.stemWord(token) for token in tokens]
