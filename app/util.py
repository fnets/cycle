import random

from models import Entry
from app import db

def get_entry():
    # extend this function to randomly return an entry, default pulls from database
    query = db.session.query(Entry)
    row_count = int(query.count())
    random_entry = query.offset(int(row_count * random.random())).first()
    return random_entry

if __name__ == '__main__':
    print get_entry()