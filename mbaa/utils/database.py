""" Module for database operations """

import sys
import time
import configparser
import mysql.connector
from mysql.connector import errorcode
from utils.message import print_message


DB_NAME = "mbaa"
SCHEMA_FILE_URL = "data/schema.sql"
SEED_FILE_URL = "data/seed.sql"
CONFIG_FILE_URL = "data/config.ini"


def load_database_credentials(url):
    """Function to load database credentials"""
    try:
        config = configparser.ConfigParser()
        config.read(url)
        database_config = config["database"]
        user = database_config["user"]
        password = database_config["password"]
        host = database_config["host"]
        print_message("mysql credentials loaded successfully", "success")
        return user, password, host
    except FileNotFoundError as file_err:
        print_message(f"Failed reading file: {file_err}", "error")
        sys.exit(1)


def connect_to_mysql():
    """Function to create the connection to the database"""
    try:
        print_message("Connecting to mysql...", "info")
        user, password, host = load_database_credentials(CONFIG_FILE_URL)
        connection = mysql.connector.connect(
            user=user, password=password, host=host, raise_on_warnings=True
        )
        print_message("Connection to mysql successful", "success")
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print_message("Something is wrong with your user name or password", "error")
        else:
            print_message(err, "error")
        sys.exit(1)


def create_database(db_name):
    """Function to create the database"""
    try:
        print_message(f"Creating database {db_name}...", "info")
        with connect_to_mysql() as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {db_name};")
        print_message(f"Database {db_name} created successfully", "success")
    except mysql.connector.Error as db_err:
        print_message(f"Failed creating database: {db_err}", "error")
        sys.exit(1)


def connect_to_database(db_name=DB_NAME):
    """Function to connect to the database"""
    try:
        print_message("Connecting to database...", "info")
        connection = connect_to_mysql()
        connection.database = db_name
        print_message(f"Connection to database {db_name} successful", "success")
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print_message(f"Database {db_name} does not exist", "warning")
            create_database(db_name)
            return connect_to_database(db_name)
        sys.exit(1)


def read_sql_file(filename):
    """Function to read sql from file"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print_message(f"Opening file: {filename}", "info")
            sql = file.read()
        print_message(f"File {filename} read successfully", "success")
        return sql
    except FileNotFoundError as file_err:
        print_message(f"Failed reading file: {file_err}", "error")
        sys.exit(1)


def create_tables_from_file(filename):
    """Function to execute sql from file"""
    print_message("Creating tables...", "info")
    sql = read_sql_file(filename)
    try:
        with connect_to_database(DB_NAME) as connection:
            connection.reconnect()
            with connection.cursor() as cursor:
                cursor.execute(sql, multi=True)
        print_message("Tables created successfully", "success")
    except FileNotFoundError as file_err:
        print_message(f"Failed reading file: {file_err}", "error")
        sys.exit(1)
    except mysql.connector.Error as sql_err:
        if sql_err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print_message("Table already exists.", "warning")
        else:
            print_message(f"Error creating tables: {sql_err}", "error")
        sys.exit(1)


def show_tables():
    """Function to show tables"""
    with connect_to_database(DB_NAME) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES;")
            for table in cursor.fetchall():
                print(table)


def populate_tables_from_file(filename):
    """Function to execute sql from file"""
    try:
        print_message("Populating tables...", "info")
        sql = read_sql_file(filename)
        with connect_to_database(DB_NAME) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, multi=True)
                for result in cursor:
                    if result.with_rows:
                        result.fetchall()
                    else:
                        print_message(f"Rows affected: {result.rowcount}", "info")
                connection.commit()
        print_message("Tables populated successfully", "success")
    except FileNotFoundError as file_err:
        print_message(f"Failed reading file: {file_err}", "error")
        sys.exit(1)
    except mysql.connector.Error as sql_err:
        if sql_err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print_message("Table already exists.", "warning")
        else:
            print_message(f"Error creating tables: {sql_err}", "error")
        sys.exit(1)


if __name__ == "__main__":
    # connect_to_database()
    create_tables_from_file(SCHEMA_FILE_URL)
    time.sleep(1)
    populate_tables_from_file(SEED_FILE_URL)
