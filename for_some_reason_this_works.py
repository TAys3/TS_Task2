import sqlite3

def commit(username, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO user VALUES (?,?)", (username,password)) #I think it breaks here, but it should work
    conn.commit()
    conn.close()