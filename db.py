import sqlite3

DATABASE = 'db/SkillPire.db'

def get_db():
    return sqlite3.connect(DATABASE)

def select(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Admin")
    data=cursor.fetchall()
    print(data)

db = get_db()
select(db)
db.close()
