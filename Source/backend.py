import sqlite3


def connect():
    conn = sqlite3.connect("Schedule.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Schedule (frame text,title text,describtion text ,hour text ,minute text, second text ,year text ,month text ,day text ,state text )")
    conn.commit()
    conn.close()


def insert(frame, title, describtion, hour, minute, second, year, month, day, state):
    conn = sqlite3.connect("Schedule.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Schedule VALUES (?,?,?,?,?,?,?,?,?,?)",
                (frame, title, describtion, hour, minute, second, year, month, day, state))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("Schedule.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Schedule")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(frame=""):
    conn = sqlite3.connect("Schedule.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Schedule WHERE frame=? ", (frame,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(frame):
    conn = sqlite3.connect("Schedule.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Schedule WHERE frame=?", (frame,))
    conn.commit()
    conn.close()


def update(frame, title, describtion, hour, minute, second, year, month, day, state):
    conn = sqlite3.connect("Schedule.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE Schedule SET title=?,describtion=?,hour=?,minute=?,second=?,year=?,month=?,day=?,state=? WHERE frame=?",
        (title, describtion, hour, minute, second, year, month, day, state, frame))
    conn.commit()
    conn.close()


def update_active(frame, state):
    conn = sqlite3.connect("Schedule.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE Schedule SET state=? WHERE frame=?",
        (state, frame))
    conn.commit()
    conn.close()


connect()
