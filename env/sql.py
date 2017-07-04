#__ create a SQLite3 table and populate it with data
import sqlite3

#__ create a new database if the database does not exist already
with sqlite3.connect("blog.db") as connection:
	#__ get a cursor object used to execute SQL commands
	c = connection.cursor()

	#__ create a table
	c.execute("CREATE TABLE posts (title TEXT, post TEXT)")

	#__insert dummy data into the table
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m well")')
	c.execute('INSERT INTO posts VALUES("Excellent", "I\'m Excellent")')
	c.execute('INSERT INTO posts VALUES("okay", "I\'m okay")')