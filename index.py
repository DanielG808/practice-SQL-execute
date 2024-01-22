from execute import execute

id = 1
username = "Dan"
password = "Gray"

execute("DROP TABLE IF EXISTS users;")

execute("CREATE TABLE users (id INTEGER NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL);")

execute("INSERT INTO users VALUES (?, ?, ?)", id, username, password)

