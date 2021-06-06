# CREATE DATABASE ss1;

CREATE TABLE ss1.Employee(
    PersonID int AUTO_INCREMENT,
    name1 varchar(255) NOT NULL,
    number1 varchar(255) NOT NULL,
    kw1 int(5),
    PRIMARY KEY (PersonID)
);

SHOW DATABASES;
SHOW TABLES;
SHOW COLUMNS FROM TABLE_NAME;
DESCRIBE TABLE_NAME;
USE ss1; -- USE A SPECIFIC DATA BASE 
--mysql -u root -p -e 'show databases;'
--mysql -u root -p

--CREATE USER 'admin'@'localhost' IDENTIFIED BY '123qwe';

# sql1 = UPDATE ss1.Employee SET name1 = "kush", number1 = "2334", kw1 = "qweasd123";
# cursor.execute('SHOW DATABASES')
# cursor.execute("UPDATE Employee SET name1 = 'kush', number1 = '2334', kw1 = 'qweasd123';")
# INSERT INTO Employee (name1, number1, kw1) VALUES ('oply','1ew21','556');
# select * from Employee where name1 = 'kraus';
# ALTER TABLE ss1.Employee ADD id_temp int NULL;
# alter table Employee drop id_temp;
# alter table Employee add idq int auto_increment key;
# DELETE FROM Employee WHERE idq = 63;