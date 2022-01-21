import io
import re
import logging
from requests import get
from bs4 import BeautifulSoup as bs
from PyPDF2 import PdfFileReader
from urllib.request import urlopen
import os

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
path = "../output"
output = "../output/"
complete_urls = []
myfiles = 0


# saving data into text file
def save(site, content, name):
    global output, myfiles
    content = re.sub(" +", " ", content)
    print(output)
    with open(output + name + ".txt", "w") as file:
        file.write(f"{site}{content}")
        file.close()
    myfiles += 1
    return myfiles


# checking links that have social links


# converting pdf into txt
def savePdf(hL):
    data = urlopen(hL).read()
    temp = io.BytesIO(data)
    pdfFile = PdfFileReader(temp)
    combine = pdfFile.getPage(0).extractText().replace("\n", "")
    combine = re.sub(" +", " ", combine)
    if len(combine.split(" ")) > 50:
        save(hL, combine, "output{0}".format(str(myfiles)))

        import tokenize

        stream = tokenize.open(myfiles)  # @UndefinedVariable
        try:
            contents = stream.read()
        finally:
            stream.close()


# seperating files
def seperatingFiles(hL):
    if hL in complete_urls != False:

        return

    if hL.endswith(".pdf"):
        savePdf(hL)

    elif hL.endswith(".txt"):
        r = get(hL, allow_redirects=False, timeout=20)
        s = bs(r.text, "html.parser")
        combine = s.get_text()
        if len(combine.split(" ")) > 50:
            save(hL, combine, "output{0}".format(str(myfiles)))
    else:
        fetch(hL)
    complete_urls.append(hL)


# getting data from each link
def fetch(site):
    global myfiles, complete_urls
    # if myfiles < 1:
    res = get(site, timeout=5)
    res_html = bs(res.text, features="html.parser")
    res_html_text = res_html.get_text()
    save(site, res_html_text, "output{0}".format(str(myfiles)))
