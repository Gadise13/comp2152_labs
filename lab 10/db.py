import sqlite3
import function
db_connection = sqlite3.connect("sqlite.db")
print(db_connection)

db_cursor = db_connection.cursor
print(db_cursor)

query1 = "SELECT + FROM demo"
db_cursor.execute(query1)
print("Reading 2 row")
row = db_cursor.fetchone()
print(row)
  
print("Reading 3 row")
row = db_cursor.fetchone()
print(r)


print("Reading all rows")
# rows = db_cursor.fetchall()
# for r in rows:
#     print(r)
function.query_responder(db_cursor, fetch_type:"fetchamany) 
    
query2 = "INSERT INTO demo (Name, Hint) values ('Gadise', 'Oli')"
db_cursor.execute(query2)
db_connection.commit()
id = input("Enter an id:")
# query3 = "SELECT * FROM demo WHERE ID >?"
# db_cursor.execute(query3, (id))
# function.query_responder(db_cursor,fetch_type=)