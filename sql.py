# sql.py - Create a SQLite3 table and populate it with data

import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as conn:
    c = conn.cursor()

    #  drop table if already exists
    c.execute("DROP TABLE if exists posts")

    # create the table
    c.execute("""CREATE TABLE posts
            (title TEXT, post TEXT)
            """)

    # insert dummy data into the table
    data = [
    ("Good", "I\'m good."),
    ("Well", "I\'m well."),
    ("Excellent", "I\'m excellent."),
    ("Okay", "I\'m okay.")
    ]

    c.executemany("INSERT INTO posts VALUES(?, ?)", data)
