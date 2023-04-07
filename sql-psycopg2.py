import psycopg2

# connect to "chinook" db

connection = psycopg2.connect(database="chinook")

# build a cursor object 

cursor = connection.cursor()

# query 1 - select all records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')

# quer2 

cursor.execute('SELECT "Name" FROM "Artist"')

#fetch

results = cursor.fetchall()

# fetch the result(single)
# results = cursor.fetchone()

#close hte connection

connection.close()

#print results 

for result in results:
    print(result)