from flask import Flask, request
from flask import render_template
from run import index_documents
from indexing_and_searching.indexing import Index
from indexing_and_searching.loading import load_documents
from threading import Thread

app = Flask(__name__)


# background task
def background():
    index = index_documents(load_documents(), Index())
    return index

# first page of the website
@app.route('/')
def my_form():
    return render_template('form.html')


index = background()


@app.route('/', methods=['POST'])
def my_form_post():
    if index:
        searching_keyword = request.form['variable']
        try:
            results = index.search(searching_keyword)
        except:
            print(index.search(searching_keyword))
        finally:
            return render_template('form.html', results=results)


if __name__ == '__main__':
    thread = Thread(target=background)
    thread.daemon = True
    thread.start()
