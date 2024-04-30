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

    id: str = str(uuid.uuid4())
    name: str = ""
    amount: float = 0
    start_date: datetime = datetime.now()
    is_recurrent: bool = False
    last_payment_date: datetime = datetime.now().date()
    next_payment_date: datetime = datetime.now().date()
    is_recurrent: bool = False
    category_id: str = ""
    budget_id: str = ""

    def create_expense(self):
        """Method to create an expense"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    if self.is_recurrent:
                        cols = [
                            "id",
                            "name",
                            "amount",
                            "start_date",
                            "last_payment_date",
                            "next_payment_date",
                            "is_recurrent",
                            "category_id",
                        ]
                        str_cols = f'({", ".join(cols)})'
                        sql = (
                            f"INSERT INTO expenses {str_cols}"
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        )
                        expense_config = [
                            str(uuid.uuid4()),
                            self.name,
                            self.amount,
                            self.start_date,
                            self.last_payment_date,
                            self.next_payment_date,
                            True,
                            self.category_id,
                        ]
                    else:
                        cols = [
                            "id",
                            "name",
                            "amount",
                            "start_date",
                            "category_id",
                            "is_recurrent",
                        ]
                        str_cols = f'({", ".join(cols)})'
                        sql = f"INSERT INTO expenses {str_cols} VALUES (%s, %s, %s, %s, %s , %s)"
                        expense_config = [
                            str(uuid.uuid4()),
                            self.name,
                            self.amount,
                            self.start_date,
                            self.category_id,
                            False,
                        ]
                    print(expense_config)
                    cursor.execute(sql, expense_config)
                    connection.commit()
                    expense_id = self.get_expense_id_by_name(self.name)
            self.create_relationship_budgets_expenses(
                expense_id, self.budget_id, self.amount
            )
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

    def get_expenses_by_budget_id(self, budget_id):
        """Method to get expenses by budget id"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = (
                        "SELECT e.name, e.amount, c.name FROM expenses as e "
                        "INNER JOIN budgets_expenses as b ON e.id = b.expense_id "
                        "INNER JOIN categories as c ON e.category_id = c.id "
                        "WHERE b.budget_id = %s"
                    )
                    cursor.execute(sql, (budget_id,))
                    expenses = cursor.fetchall()
                    return expenses
        except mysql.connector.Error as error:
            print_message(f"Error getting expenses: {error}", "error")
            return []

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
                    print(relationship_config)
                    cursor.execute(sql, relationship_config)
                    connection.commit()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Relationship already exists.")
            else:
                print(f"Error creating relationship: {error}")
                raise error
