import regex as re
import sqlite3 as sq3
from sys import argv
#HTML5 utilise UTF-8
phase3_results = open(argv[1], 'r', encoding="UTF-8").read()
posologies = re.findall('<a href="[0-9 ]+?">(.*?)</a>', phase3_results)
db = sq3.connect("extraction.db")
control = db.cursor()
control.execute("DROP TABLE IF EXISTS Treatment")
control.execute("CREATE TABLE IF NOT EXISTS Treatment (id INT PRIMARY KEY NOT NULL, posologie TEXT NOT NULL )")
control.executemany("INSERT INTO Treatment VALUES (?,?)", enumerate(posologies, start=1))
print("Insertion completed")
db.commit()
db.close()