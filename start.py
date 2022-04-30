from app.db_model import db, URLMapping
from app import create_app
from uuid import uuid4

app = create_app(db)
with open("key.txt", "w+") as fh:
    app.secret_key = fh.readline()
    if not app.secret_key:
        key = str(uuid4()).replace('-', '')
        app.secret_key = key

        fh.write(key)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=False)