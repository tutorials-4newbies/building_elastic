import time
from pprint import pprint

from building_elastic.load import load_reviews
from building_elastic.naive_search import Index

if __name__ == "__main__":
    documents = load_reviews()
    index = Index(documents=documents)
    while True:
        query = input("ask me anything: ")
        start_time = time.time()
        result = index.search(query)
        pprint(result)
        end_time = time.time()
        print(f"Query took: {end_time - start_time}")

