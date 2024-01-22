import sqlite3

connection = sqlite3.connect('practice.db')

crsr = connection.cursor()

def execute(query):
    return crsr.execute(query)
    