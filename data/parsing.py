import sqlite3

con = sqlite3.connect('../db/sites_base.sqlite')
cur = con.cursor()
rows = len(cur.execute("SELECT * FROM sites").fetchall())
titels = cur.execute("SELECT name FROM sites").fetchall()
print(titels)