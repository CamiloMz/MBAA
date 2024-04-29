""" Module for test model """

import time
from dataclasses import dataclass

from models.budget_model import Budget

from models.expense_model import Expense
from models.categories_model import Categories
from utils.message import print_message
import mysql.connector
from mysql.connector import errorcode


@dataclass
class TestModel:
    """Class for test model"""

    def list_categories_test(self):
        """Function to list categories"""
        categories_list = Categories().get_all_categories()
        return categories_list

    def create_category_test(self, name_category, category_type):
        """Function to create a category"""
        category_name = name_category.capitalize()
        category_type = category_type.capitalize()
        try:
            category = Categories().get_category_by_name(category_name)[0]

            if category:
                print_message("Category already exists.", "warning")
                return category[0]

            category = Categories(name=category_name, type=category_type)
            category.create_category()
            print_message(f"Category {category_name} created.", "info")
            print(category)
            time.sleep(1)
            category_id = Categories().get_category_by_name(category_name)
            print(category_id)
            return category_id
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print_message("Category already exists.", "warning")
            else:
                print_message(f"Error creating category: {error}", "error")
            return None

    def edit_category_test(self, category_info: dict):
        """Function to edit a category"""
        try:
            print(category_info)
            category = Categories().get_category_by_name(category_info["name_category"])
            print(category)
            if not category:
                print_message("Category does not exist.", "warning")
                return None
            category = Categories(
                id=category_info["id_category"],
                name=category_info["name_category"],
                type=category_info["category_type"],
            )
            print("category")
            print(category)
            category.update_category()
            time.sleep(1)
            return category
        except mysql.connector.Error as error:
            print_message(f"Error updating category: {error}", "error")
            return None

    def get_category_id_by_name_test(self, name):
        """Function to get category by name"""
        category_id = Categories().get_category_by_name(name)[0]
        return category_id

    def list_budgets_test(self):
        """Function to list budgets"""
        budget_list = Budget().get_all_budgets()
        return budget_list

    def create_budget_test(self, budget_info: dict):
        """Function to create a budget"""
        try:
            budget = Budget().get_budget_by_name(budget_info["name_budget"])
            if budget:
                print_message("Budget already exists.", "warning")
                return budget[0]
            budget = Budget(
                name=budget_info["name_budget"],
                initial_amount=budget_info["initial_amount"],
                final_amount=budget_info["initial_amount"],
                date=budget_info["date"],
                category_id=budget_info["category_id"],
            )
            budget.create_budget()
            time.sleep(1)
            budget_id = Budget().get_budget_id_by_name(budget_info["name_budget"])
            return budget_id
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print_message("Budget already exists.", "warning")
            else:
                print_message(f"Error creating budget: {error}", "error")
            return None

    def get_budget_id_by_name_test(self, name):
        """Function to get budget by name"""
        budget_id = Budget().get_budget_id_by_name(name)
        return budget_id

    def get_budget_by_name_test(self, name):
        """Function to get budget by name"""
        budget = Budget().get_budget_by_name(name)
        return budget

    def list_expenses_test(self):
        """Function to list expenses"""
        expenses_list = Expense().get_all_expenses()
        return expenses_list

    def create_expense_test(self, expense_info: dict):
        """Function to create an expense"""
        try:
            expense = Expense().get_expense_by_name(expense_info["name_expense"])
            if expense:
                print_message("Expense already exists.", "warning")
                return expense[0]
            expense = Expense(
                name=expense_info["name_expense"],
                amount=expense_info["amount"],
                start_date=expense_info["start_date"],
                category_id=expense_info["category_id"],
                budget_id=expense_info["budget_id"],
            )
            expense.create_expense()
            time.sleep(1)
            expense_id = Expense().get_expense_id_by_name(expense_info["name_expense"])
            return expense_id
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print_message("Expense already exists.", "warning")
            else:
                print_message(f"Error creating expense: {error}", "error")
            return None
