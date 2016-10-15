import os


os.environ['CFG_TYPE'] = 'dev'


if __name__ == '__main__':
    from app import app
    app.run(host="0.0.0.0")
