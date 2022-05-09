from uuid import uuid4
from os.path import isfile

from app.db import db
from app import create_app
from app.login import login_manager

app = create_app(db, login_manager)

if isfile('key.txt'):
    with open('key.txt', "r") as fh:
        app.secret_key = fh.readline()
else: 
    with open("key.txt", "w+") as fh:
        key = str(uuid4()).replace('-', '')
        app.secret_key = key
        
        fh.write(key)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)