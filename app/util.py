from config import entries
from random import choice

def get_entry():
    # idea is to extend this to randomly pull from a csv, sqlite, or web crawler
    entry = choice(entries)
    return entry