import re
import string

STOPWORDS = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
                 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
                 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'movie'])

PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))

def punctuation_filter(tokens):
    return [PUNCTUATION.sub('', token) for token in tokens]
