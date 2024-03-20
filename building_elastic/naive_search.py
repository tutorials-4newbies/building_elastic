from typing import List

from building_elastic.value_objects import Response, Review


class Index:
    def __init__(self, documents:List[Review]):
        self.documents = documents

    def search(self, query:str) -> Response:
        count = 0
        candidates = []
        for document in self.documents:
            if query in document.text:
                count +=1
                candidates.append(document)
        return Response(count=count, samples=candidates[0:10])
