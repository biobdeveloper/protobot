CREATE ROLE protobot_user LOGIN SUPERUSER PASSWORD 'protobot_pass';
CREATE DATABASE protobot_db owner protobot_user;