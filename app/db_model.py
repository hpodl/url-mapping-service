from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URLMapping(db.Model):
    custom_url = db.Column(db.String(50), primary_key=True)
    target_url = db.Column(db.String(100), nullable=False)

    def __init__(self, custom, target):
            self.custom_url = custom
            self.target_url = target

    def __repr__(self):
        return '<%r -> %r>' % (self.custom_url, self.target_url)