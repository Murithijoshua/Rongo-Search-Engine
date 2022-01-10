from app import app

if __name__ == '__main__':
    thread = Thread(target=background)
    thread.daemon = True
    thread.start()
    app.run()