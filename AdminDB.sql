CREATE DATABASE AdminDB;
use AdminDB;
CREATE TABLE admins (
id int not null auto_increment,
username varchar(255),
password varchar(255),
primary key (id));

CREATE TABLE ids (
id int not null auto_increment,
monitor varchar(255),
keyboard varchar(255),
mouse varchar(255),
primary key (id));

INSERT INTO admins(username, password) VALUES ("admin", "admin123");