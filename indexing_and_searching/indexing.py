from processor.preprocessor import cleaning_query
import math


class Index:
    def __init__(self):
        self.index = {}
        self.documents = {}

    # indexing docs and tokens
    def index_document(self, document):
        if document.id not in self.documents:
            self.documents[document.id] = document
            # frequency counts when we index our data
            document.analyze()
        # indexing token in each individual document
        for token in cleaning_query(document.text):
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(document.id)

    # occurrences of a word in x number of documents
    def document_frequency(self, token):
        return len(self.index.get(token, set()))

    # inverse of document_frequency
    def inverse_document_frequency(self, token):  #
        return math.log10(len(self.documents) / self.document_frequency(token))

    def _results(self, analyzed_query):
        return [self.index.get(token, set()) for token in analyzed_query]

    # searching token/tokens  inside a document
    def search(self, query, search_type='AND', rank=True):
        analyzed_query = cleaning_query(query)
        if len(analyzed_query)==0:
            return []

        results = self._results(analyzed_query)
        if search_type == 'AND':
            # all tokens must be in the document
            documents = [self.documents[doc_id] for doc_id in set.intersection(*results)]
        if search_type == 'OR':
            # only one token has to be in the document
            documents = [self.documents[doc_id] for doc_id in set.union(*results)]

        if rank:
            return self.rank(analyzed_query, documents)
        return documents

    def rank(self, analyzed_query, documents):
        results = []
        if not documents:
            return results
        for document in documents:
            score = 0.0
            for token in analyzed_query:
                tf = document.term_frequency(token)
                idf = self.inverse_document_frequency(token)
                score += tf * idf
            results.append((document, score))
            # after computing the score, the i go ahead to sort them descending order
        return sorted(results, key=lambda doc: doc[1], reverse=True)
