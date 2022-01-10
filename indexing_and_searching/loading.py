import os
from indexing_and_searching.documents import Data

# loading data into memory for further operations
def load_documents():
    path = "../output"
    output = r"output/"
    os.chdir(output)
    # iterate through all files
    number = 1
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            with open(file_path, 'r') as f:
                p = f.read()
                link = p.split()[0]
                text = (p.split()[1:])
                txt = " ".join(text)
                number += 1
            yield Data(id=number, text=txt, url=link)
