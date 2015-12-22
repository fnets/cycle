from app import db

class Entry(db.Model):
    __tablename__ = 'entry'
    entry_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    director = db.Column(db.String(128), index=True)
    release_year = db.Column(db.Integer, index=True)
    stars = db.relationship('Star', back_populates='entry')

    def __repr__(self):
        return '<Entry %r>' % (self.name)

class Star(db.Model):
    __tablename__ = 'star'
    star_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.entry_id'))
    entry = db.relationship('Entry', back_populates='stars')

    def __repr__(self):
        return '<Star %r>' % (self.name)