import os

import pandas as pd

from building_elastic.value_objects import Review

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_reviews():
    df = pd.read_csv(os.path.join(base_path, 'data/IMDB Dataset.csv.zip'), compression='zip')
    reviews = df['review'].to_list()
    results = []
    for idx, text in enumerate(reviews):
        review = Review(identifier=idx, text=text)
        results.append(review)
    return results
