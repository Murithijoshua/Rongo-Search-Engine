import io
import re
import logging
from requests import get
from bs4 import BeautifulSoup as bs
from PyPDF2 import PdfFileReader
from urllib.request import urlopen
import os

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
path = f"{os.getcwd()}/output"
output = r"output/"

complete_urls = []
myfiles = 0


# saving data into text file
def save(site, content, name):
    global output, myfiles
    content = re.sub(" +", " ", content)
    if countWords(content):
        with open(output + name + ".txt", "w") as file:
            file.write(f"{site}{content}")
            file.close()
        myfiles += 1
        return myfiles


# checking links that have social links
def find_social_link(link):
    socialLinks = ["google", "youtube","twitter","instagram","linkedin"]
    return any(i in link for i in socialLinks)


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
def seperatingFiles(link):
    if hL in complete_urls or find_social_link(hL) != False:

        return

    if hL.endswith(".pdf"):
        savePdf(hL)

    elif hL.endswith(".txt"):
        r = get(hL, allow_redirects=False, timeout=20)
        s = bs(r.text, "html.parser")
        combine = s.get_text()
        if len(combine.split(" ")) > 50:
            save(hL,combine, "output{0}".format(str(myfiles)))
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
    if len(res_html_text) > 0:
        save(site, res_html_text, "output{0}".format(str(myfiles)))
