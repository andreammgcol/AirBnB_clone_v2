-- script that creates a database hbnb_dev_db with a user hbnb_dev
--
CREATE DATABASE IF NOT EXISTS hbnb_dev_db
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON * . * TO hbnb_dev@localhost;
GRANT ALL PRIVILEGES ON performance_schema. * TO hbnb_dev@localhost;
