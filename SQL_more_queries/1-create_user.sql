-- Creates the MySQL server user user_0d_1 if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges to the user user_0d_1 on the MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Applies the privilege changes
FLUSH PRIVILEGES;
