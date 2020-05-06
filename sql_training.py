import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user1 = (1, 'athul', '123')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user1)
print (user1)

user2 = (2, 'jarvis', '456')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user2)
print (user2)

user3 = (3, 'friday', '789')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user3)
print (user3)

user4 = (4, 'peter', '12345')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user4)
print (user4)

user5 = (5, 'parker', '67890')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user5)
print (user5)


connection.commit()
connection.close()
