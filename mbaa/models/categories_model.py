""" Model for categories"""

import uuid
from dataclasses import dataclass
from utils.database import connect_to_database
from utils.message import print_message
import mysql.connector
from mysql.connector import errorcode


@dataclass
class Categories:
    """Class for categories model"""

    id: str = uuid.uuid4().hex
    name: str = None
    type: str = None

    def create_category(self):
        """Method to create a category"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO categories (id, name, type) VALUES (%s, %s, %s)"
                    category_config = (self.id, self.name, self.type)
                    cursor.execute(sql, category_config)
                    connection.commit()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print_message("Category already exists.", "warning")
            else:
                print_message(f"Error creating category: {error}", "error")

    def get_all_categories(self):
        """Method to get all categories"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM categories")
                    categories = cursor.fetchall()
                    return categories
        except mysql.connector.Error as error:
            print_message(f"Error getting categories: {error}", "error")
            return []

    def get_category_by_name(self, name):
        """Method to get category by name"""
        print_message(f"searching for category {name}", "info")
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM categories WHERE name = %s"
                    cursor.execute(sql, (name,))
                    category = cursor.fetchone()
                    return category
        except mysql.connector.Error as error:
            print_message(f"Error getting category: {error}", "error")
            return None

    def get_category_id_by_name(self, name):
        """Method to get category by name"""
        print_message(f"searching for category {name}", "info")
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT id FROM categories WHERE name = %s"
                    cursor.execute(sql, (name,))
                    category = cursor.fetchone()
                    return category[0]
        except mysql.connector.Error as error:
            print_message(f"Error getting category: {error}", "error")
            return None
