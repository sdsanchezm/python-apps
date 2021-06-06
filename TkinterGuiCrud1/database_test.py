import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "admin",
    passwd = "123qwe",
    database = "ss1"
)

cursor = db.cursor()
# execute 
cursor.execute("SHOW DATABASES")

# the list of databases is stored in 'databases'
databases = cursor.fetchall()

# who all databases in a single line: 
print(databases)

## show all databases line per line 
for database in databases:
    print(database)

#sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"


# sql1 = UPDATE ss1.Employee SET name1 = "kush", number1 = "2334", kw1 = "qweasd123";
# cursor.execute('SHOW DATABASES')
# cursor.execute("UPDATE Employee SET name1 = 'kush', number1 = '2334', kw1 = 'qweasd123';")
# INSERT INTO Employee (name1, number1, kw1) VALUES ('oply','1ew21','556');
# select * from Employee where name1 = 'kraus';
# ALTER TABLE ss1.Employee ADD id_temp int NULL;
# alter table Employee drop id_temp;
# alter table Employee add idq int auto_increment key;

sql1 = "INSERT INTO Employee (name1, number1, kw1) VALUES ('banu','ee998','332')"

cursor.execute(sql1)

db.commit()
print(cursor.rowcount, "record(s) affected")

# asd
sql1 = "SELECT * FROM Employee"
cursor.execute(sql1)
# db.commit()
print(cursor.rowcount, "record(s) affected")



