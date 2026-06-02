import os
import pymysql

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables
mysql_password= os.getenv("MYSQL_PASSWORD")

def connect_db():
    try:
        connection = pymysql.connect(user = "dev", password = mysql_password, port = 3306, database="world", charset="utf8", host="localhost")
        print("DB connected")
        return connection;
    except:
        print("DB connection failed")

def disconnect_db(connection):
    try:
        connection.close()
        print("DB disconnected")
    except:
        print("DB disconnection failed")

def create_table():
    query = "create table if not exists people(id int primary key auto_increment, name varchar(64) not null, gender bool not null, age int default(0),location varchar(32));"
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print("Table created (if it didn't exist)")
        else:
            print("Table creation failed")
        cursor.close()
        disconnect_db(connection)
        
    except:
        print("Table creation error")
    
def create_db():
    query = "create database world;"
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print("DB created")
        else:
            print("DB creation failed")
        cursor.close()
        disconnect_db(connection)
        
    except:
        print("DB creation error")
