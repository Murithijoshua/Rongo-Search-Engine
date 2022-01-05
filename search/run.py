from pprint import pprint
from indexing_and_searching.loading import load_documents
from indexing_and_searching.indexing import Index


# indexing the corpus in the memory
def index_documents(documents, index):
    for i, document in enumerate(documents):
        index.index_document(document)

        print(f'Indexed {i} documents', end='\r')
    return index


if __name__ == '__main__':
    def start():
        index = index_documents(load_documents(), Index())
        while index:
            results = []
            searching_keyword = input("Enter Your query or QUIT stop program running: ")
            if searching_keyword.upper() == "QUIT":
                index = False
            p = index.search(searching_keyword)
            pprint(p)


    start()
