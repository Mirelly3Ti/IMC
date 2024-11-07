import sqlite3

def init_db():
    conn = sqlite3.connect('imc.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRYMARY KEY AUTOPINCREMENT,
            nome TEXT NOT NULL,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            IMC REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()