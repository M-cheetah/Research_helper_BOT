import sqlite3
import csv

con=sqlite3.connect("base.db")

con.execute("CREATE TABLE IF NOT EXTSTS database (Coin CHAR(10), CurrentPrice double, Close double, Volume double);")

con.commit()

with open('record.csv') as file:
	reader=csv.reader(file)
	
for row in reader:
	coin=row[0]
	current_price=row[1]
	close=row[2]
	volume=row[3]
	con.execute("INSERT INTO database values('"+coin+"','"+current+"','"+close+"','"volume"');")
	con.commit()

