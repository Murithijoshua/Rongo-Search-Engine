from collections import Counter
from dataclasses import dataclass
from processor.preprocessor import cleaning_query

# since i am not saving the corpus inside the txt file, in this case Iam saving it in memory
# i needed dataclass to create identity of individual document
# speed - querying nd insertion
@dataclass
class Data:
    id: int
    text: str
    url: str
    #count words inside a document
    def analyze(self):
        self.term_frequencies = Counter(cleaning_query(self.text))

    def term_frequency(self, term):
        # helper method that means incase a word has count it is then incremented for instance get : 1 once it
        # reappears it will be get:2
        return self.term_frequencies.get(term, 0)

    def __repr__(self) -> str:
        return f'{self.url}'
