""" Module for categories controller """

import uuid
from models.categories_model import Categories, get_category_by_name
from utils.message import print_message
import mysql.connector
from mysql.connector import errorcode


class CategoriesController:
    """Class for categories controller"""

    @staticmethod
    def create_category(category_name, category_type):
        """Method to create a category"""
        try:
            category = get_category_by_name(category_name)

            if category:
                print_message("Category already exists.", "warning")
                return category[0]

            category = Categories(
                id=str(uuid.uuid4()), name=category_name, type=category_type
            )
            category.create_category()
            return True
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print_message("Category already exists.", "warning")
            else:
                print_message(f"Error creating category: {error}", "error")
            return False
