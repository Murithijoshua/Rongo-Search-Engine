import re
import string
from spacy.lang.en.stop_words import STOP_WORDS as stop_words
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# converting texts into lowercase

stemmer = PorterStemmer()


# to lowercase
def lower(text: str):
    return [text.lower()]


# removing numbers 0-9
def remove_numbers(text: str):
    return re.sub(r"\d+", "", text)


# removing punctuations
def remove_punctuations(text):
    return text.translate(str.maketrans("", "", string.punctuation))


# removing white spaces
def removing_whitespaces(text: str):
    return text.strip()


# removing stop words
def removing_stop_words(text: str):
    token = word_tokenize(text)
    return [i for i in token if i not in stop_words]


# stemming
def stemming(text):
    return [stemmer.stem(txt) for txt in text]

# read reading txt files
def read_text_file(file_path):
    with open(file_path, "r") as f:
        txt = _extracted_from_read_text_file_3(f)

    with open(file_path, "w") as f:
        f.write(txt)

    return txt.split(" ")


def _extracted_from_read_text_file_3(f):
    result = f.read()
    # to lower case
    result = lower(result)
    result = remove_numbers(result)
    result = remove_punctuations(result)
    result = removing_whitespaces(result)
    result = removing_stop_words(result)
    result = stemming(result)
    return result


def cleaning_query(result: str):
    result = remove_numbers(result)
    result = lower(result)
    result = remove_punctuations(' '.join(result))
    result = removing_whitespaces(result)
    result = removing_stop_words(result)
    result = stemming(result)
    return [token for token in result if token]

# checking number each word/token is unique in each document
