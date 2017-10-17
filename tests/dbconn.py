import sqlite3
conn = sqlite3.connect('ejemplo.db')


c = conn.cursor()
#c.execute("CREATE TABLE paraules (par text, count integer)")
#c.execute("INSERT INTO paraules VALUES('bdssm', 0)")
conn.commit()

c.execute("SELECT * FROM paraules")
for row in c:
	print row[0]

conn.close()