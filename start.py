from app.db_model import db, URLMapping
from app import create_app

app = create_app(db)
with open("key.txt", "r") as fh:
    app.secret_key = fh.readline()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)