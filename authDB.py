import sqlite3
import hashlib

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE user_pin (
    user text,
    pin text
    )""")

# cur.execute("DROP TABLE user_pin")

string = "1234"
hashed = hashlib.sha256((string).encode('utf-8')).hexdigest()
cur.execute("INSERT INTO user_pin VALUES (?,?)", ("Taylor", hashed))
conn.commit()
conn.close()