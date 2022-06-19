import sqlite3

with sqlite3.connect("NUM_DB.db") as db:
	cursor = db.cursor()

	cursor.execute("""CREATE TABLE IF NOT EXISTS num_db(
		number TEXT
	)""")

	values = [
		("K156KE196",),
		("Y005OP47",)
	]

	cursor.executemany("INSERT INTO num_db(number) VALUES(?)", (values))