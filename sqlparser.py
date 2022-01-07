import sqlite3
import json
connection = sqlite3.connect(":memory:")


cursor = connection.cursor()


sql_file = open("sample1.sql")

sql_as_string = sql_file.read()

cursor.executescript(sql_as_string)

list=[]
for rows in cursor.execute("SELECT * FROM airports"):
   
    print(rows)
    list.append(rows)


tojson=json.dumps(list)
    

jsonText = open('users.json', 'wb+')
jsonText.write(bytes(tojson, 'utf8'))
jsonText.close()