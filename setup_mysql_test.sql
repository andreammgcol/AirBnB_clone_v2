-- script that creates a database hbnb_test_db with a user hbnb_test
--
CREATE DATABASE IF NOT EXISTS hbnb_test_db
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON * . * TO hbnb_test@localhost;
GRANT ALL PRIVILEGES ON performance_schema. * TO hbnb_test@localhost;
