""" This module contains the test functions for the Budget App """

import uuid
import time

from models.budget import Budget, get_budget_id_by_name, get_budget_by_name
from models.expense import (
    Expense,
    get_expense_id_by_name,
    get_expense_by_name,
    create_relationship_budgets_expenses,
)
from models.categories import Categories, get_category_id_by_name, get_category_by_name
from utils.message import print_message
import mysql.connector
from mysql.connector import errorcode


def create_category_test(name_category, category_type):
    """Function to create a category"""
    category_name = name_category.capitalize()
    category_type = category_type.capitalize()
    print(f"category_name: {category_name}")
    print(f"category_type: {category_type}")
    try:
        category = get_category_by_name(category_name)

        if category:
            print_message("Category already exists.", "warning")
            return category[0]

        category = Categories(
            id=str(uuid.uuid4()), name=category_name, type=category_type
        )
        print("category: ")
        print(category)
        category.create_category()
        time.sleep(1)
        category_id = get_category_id_by_name(category_name)
        return category_id
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print_message("Category already exists.", "warning")
        else:
            print_message(f"Error creating category: {error}", "error")
        return None


def create_budget_test():
    """Function to create a budget"""
    name_category = "my_test_from_budget"
    name_budget = "Salary"
    category_type = "budget"
    initial_amount = 1000.00
    final_amount = 1000.00
    date = "2020-12-01"
    try:
        category_id = create_category_test(name_category, category_type)
        budget = get_budget_by_name(name_budget)
        if budget:
            print_message("Budget already exists.", "warning")
            return budget[0]
        budget = Budget(
            id=str(uuid.uuid4()),
            name=name_budget,
            initial_amount=initial_amount,
            final_amount=final_amount,
            date=date,
            category_id=category_id,
        )
        budget.create_budget()
        time.sleep(1)
        budget_id = get_budget_id_by_name(name_budget)
        return budget_id
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print_message("Budget already exists.", "warning")
        else:
            print_message(f"Error creating budget: {error}", "error")
        return None


def create_expense_test():
    """Function to create an expense"""
    name_category = "my_test_from_expense"
    budget_name = "Salary"
    category_type = "expense"
    expense_name = "Rent"
    try:
        category_id = create_category_test(name_category, category_type)
        budget_id = get_budget_id_by_name(budget_name)
        expense = get_expense_by_name(expense_name)
        amount = 500.00
        if expense:
            print_message("Expense already exists.", "warning")
            create_relationship_budgets_expenses(expense[0], budget_id, amount)
            return expense[0]
        expense = Expense(
            id=str(uuid.uuid4()),
            name=expense_name,
            amount=amount,
            start_date="2020-12-01",
            end_date="2020-12-31",
            category_id=category_id,
        )
        expense.create_expense()
        time.sleep(1)
        budget = get_budget_by_name(budget_name)
        new_budget = Budget(
            id=budget_id,
            name=budget_name,
            initial_amount=budget[2],
            final_amount=float(budget[3]) - float(amount),
            date=budget[4],
            category_id=budget[5],
        )
        new_budget.update_budget()
        expense_id = get_expense_id_by_name(expense_name)
        create_relationship_budgets_expenses(expense_id, budget_id, amount)
        return expense_id
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print_message("Expense already exists.", "warning")
        else:
            print_message(f"Error creating expense: {error}", "error")


if __name__ == "__main__":
    create_category_test("my_test_from_script", "expense")
    create_budget_test()
    create_expense_test()
