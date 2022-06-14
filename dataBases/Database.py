import sqlite3


with sqlite3.connect("database.db") as db:
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS users(
		login TEXT,
		password TEXT,
		username TEXT
	)""")

	cursor.execute("SELECT * FROM users")
