""" Module for expense model """

import uuid
from datetime import datetime
from dataclasses import dataclass
from utils.database import connect_to_database
from utils.message import print_message
import mysql.connector
from mysql.connector import errorcode


@dataclass
class Expense:
    """Class for expense model"""

    id: str = uuid.uuid4().hex
    name: str
    amount: float = 0
    start_date: datetime = datetime.now()
    end_date: datetime = datetime.now()
    category_id: str

    def create_expense(self):
        """Method to create an expense"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    cols = [
                        "id",
                        "name",
                        "amount",
                        "start_date",
                        "end_date",
                        "category_id",
                    ]
                    str_cols = f'({", ".join(cols)})'
                    sql = (
                        f"INSERT INTO expenses {str_cols}"
                        "VALUES (%s, %s, %s, %s, %s, %s)"
                    )
                    expense_config = [
                        self.id,
                        self.name,
                        self.amount,
                        self.start_date,
                        self.end_date,
                        self.category_id,
                    ]
                    cursor.execute(sql, expense_config)
                    connection.commit()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Expense already exists.")
            else:
                print(f"Error creating expense: {error}")
                raise error

    def get_all_expenses(self):
        """Method to get all expenses"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM expenses")
                    expenses = cursor.fetchall()
                    return expenses
        except mysql.connector.Error as error:
            print_message(f"Error getting expenses: {error}", "error")
            return []

    def get_expense_by_name(self, name):
        """Method to get expense by name"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM expenses WHERE name = %s"
                    cursor.execute(sql, (name,))
                    expense = cursor.fetchone()
                    return expense
        except mysql.connector.Error as error:
            print_message(f"Error getting expense: {error}", "error")
            return None

    def get_expense_id_by_name(self, name):
        """Method to get expense by name"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT id FROM expenses WHERE name = %s"
                    cursor.execute(sql, (name,))
                    expense_id = cursor.fetchone()
                    return expense_id[0]
        except mysql.connector.Error as error:
            print_message(f"Error getting expense: {error}", "error")
            return None

    def create_relationship_budgets_expenses(self, expense_id, budget_id, amount):
        """Method to create a relationship between expense and budget"""
        try:
            print_message("Creating relationship...", "info")
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = (
                        "INSERT INTO budgets_expenses (expense_id, budget_id, amount)"
                        "VALUES (%s, %s, %s)"
                    )
                    relationship_config = (expense_id, budget_id, amount)
                    cursor.execute(sql, relationship_config)
                    connection.commit()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Relationship already exists.")
            else:
                print(f"Error creating relationship: {error}")
                raise error
