""" Module for budget model """

import uuid
from dataclasses import dataclass
from datetime import datetime
from utils.database import connect_to_database
from utils.message import print_message
import mysql.connector
from mysql.connector import errorcode


@dataclass
class Budget:
    """Class for budget model"""

    id: str = str(uuid.uuid4())
    name: str = ""
    amount: float = 0
    date: datetime = datetime.now()
    category_id: str = ""

    def create_budget(self):
        """Method to create a budget"""
        try:
            print_message("Creating budget...", "info")
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    fields_str = [
                        "id",
                        "name",
                        "amount",
                        "date",
                        "category_id",
                    ]
                    sql = (
                        f'INSERT INTO budgets ({", ".join(fields_str)})'
                        "VALUES (%s, %s, %s, %s, %s)"
                    )
                    budget_config = (
                        str(uuid.uuid4()),
                        self.name,
                        self.amount,
                        self.date,
                        self.category_id,
                    )
                    print(budget_config)
                    cursor.execute(sql, budget_config)
                    connection.commit()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print_message("Budget already exists.", "warning")
            else:
                print_message(f"Error creating budget: {error}", "error")

    def update_budget(self):
        """Method to update a budget"""
        try:
            print_message("Updating budget...", "info")
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    set_cols = [
                        "name = %s",
                        "amount = %s",
                        "date = %s",
                        "category_id = %s",
                    ]
                    set_str = ", ".join(set_cols)
                    sql = "UPDATE budgets " f"SET {set_str} " "WHERE id = %s"
                    budget_config = (
                        self.name,
                        self.amount,
                        self.date,
                        self.category_id,
                        self.id,
                    )
                    cursor.execute(sql, budget_config)
                    connection.commit()
        except mysql.connector.Error as error:
            print_message(f"Error updating budget: {error}", "error")

    def get_all_budgets(self):
        """Method to get all budgets"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM budgets")
                    budgets = cursor.fetchall()
                    return budgets
        except mysql.connector.Error as error:
            print_message(f"Error getting budgets: {error}", "error")
            return []

    def get_budget_by_name(self, name):
        """Method to get budget by name"""
        try:
            print_message(f"searching for budget {name}", "info")
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM budgets WHERE name = %s"
                    cursor.execute(sql, (name,))
                    budget = cursor.fetchone()
                    return budget
        except mysql.connector.Error as error:
            print_message(f"Error getting budget: {error}", "error")
            return None

    def get_budget_id_by_name(self, name):
        """Method to get budget by name"""
        try:
            with connect_to_database() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT id FROM budgets WHERE name = %s"
                    cursor.execute(sql, (name,))
                    budget_id = cursor.fetchone()
                    return budget_id[0]
        except mysql.connector.Error as error:
            print_message(f"Error getting budget: {error}", "error")
            return None
