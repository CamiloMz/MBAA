""" Model for categories"""

import uuid
from dataclasses import dataclass
from utils.database import connect_to_database
import mysql.connector
from mysql.connector import errorcode


@dataclass
class Categories:
    """Class for categories model"""

    id: str = str(uuid.uuid4())
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
            result = (self, "success", f"Category {self.name} created successfully")
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                result = (None, "warning", f"Category {self.name} already exists")
            else:
                result = (None, "error", f"Error creating category: {error}")
        return result

    def get_all_categories(self):
        """Method to get all categories"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM categories")
                    categories = cursor.fetchall()
                    result = (
                        categories,
                        "success",
                        "Categories retrieved successfully",
                    )
        except mysql.connector.Error as error:
            result = (None, "error", f"Error getting categories: {error}")
        return result

    def get_all_categories_by_type(self, category_type):
        """Method to get all categories by type"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM categories WHERE type = %s"
                    cursor.execute(sql, (category_type,))
                    categories = cursor.fetchall()
                    result = (
                        categories,
                        "success",
                        "Categories retrieved successfully",
                    )
        except mysql.connector.Error as error:
            result = (None, "error", f"Error getting categories: {error}")
        return result

    def get_category_by_name(self, category_name):
        """Method to get category by name"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM categories WHERE name = %s"
                    cursor.execute(sql, (category_name,))
                    category = cursor.fetchone()
                    result = (category, "success", "Category retrieved successfully")
                    print(result)
        except mysql.connector.Error as error:
            result = (None, "error", f"Error getting category: {error}")
        return result

    def get_category_by_id(self, category_id):
        """Method to get category by id"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM categories WHERE id = %s"
                    cursor.execute(sql, (category_id,))
                    category = cursor.fetchone()
                    result = (category, "success", "Category retrieved successfully")
        except mysql.connector.Error as error:
            result = (None, "error", f"Error getting category: {error}")
        return result

    def update_category(self):
        """Method to update a category"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    set_cols = [
                        "name = %s",
                        "type = %s",
                    ]
                    set_str = ", ".join(set_cols)
                    sql = "UPDATE categories " f"SET {set_str} " "WHERE id = %s"
                    category_config = (
                        self.name,
                        self.type,
                        self.id,
                    )
                    cursor.execute(sql, category_config)
                    connection.commit()
            result = (self, "success", f"Category {self.name} updated successfully")
        except mysql.connector.Error as error:
            result = (None, "error", f"Error updating category: {error}")
        return result

    def delete_category(self):
        """Method to delete a category"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "DELETE FROM categories WHERE id = %s"
                    cursor.execute(sql, (self.id,))
                    connection.commit()
            result = (self, "success", f"Category {self.name} deleted successfully")
        except mysql.connector.Error as error:
            result = (None, "error", f"Error deleting category: {error}")
        return result
