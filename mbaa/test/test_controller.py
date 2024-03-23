""" Module for test controller """

from datetime import datetime
from dataclasses import dataclass
from test.test_model import TestModel
from test.test_view import TestView


@dataclass
class TestController:
    """Class for test controller"""

    model = TestModel()
    view = TestView()

    def run_test(self):
        """Method to run test"""
        self.categories_list_controller()
        self.create_category_controller()
        self.budget_list_controller()
        self.create_budget_controller()
        self.expense_list_controller()
        self.create_expense_controller()
        self.view.run_view()

    def categories_list_controller(self):
        """Method to list categories"""
        categories_list = self.model.list_categories_test()
        self.view.categories_list_view(categories_list)

    def create_category_controller(self, action="GET"):
        """Method to create a category"""
        if action == "POST":
            name_category = self.view.category_name_entry.get()
            category_type = self.view.category_type_select.get()
            category_id = self.model.create_category_test(name_category, category_type)
            if category_id:
                self.view.categories_tree.insert(
                    "",
                    "end",
                    values=(name_category, category_type),
                )
                self.view.category_name_entry.delete(0, "end")
                self.view.category_type_select.delete(0, "end")
                self.view.category_type_select.current(0)
                categories = self.model.list_categories_test()
                categories = [category[1] for category in categories]
                self.view.budget_category_select["values"] = categories
        else:
            self.view.category_main_button.config(
                command=lambda: self.create_category_controller("POST")
            )
            self.view.create_category_view()

    def budget_list_controller(self):
        """Method to list budgets"""
        budget_list = self.model.list_budgets_test()
        print(budget_list)
        self.view.budget_list_view(budget_list)

    def create_budget_controller(self, action="GET"):
        """Method to create a budget"""
        if action == "POST":
            name_budget = self.view.budget_name_entry.get()
            initial_amount = self.view.budget_initial_amount_entry.get()
            category_name = self.view.budget_category_select.get()
            category_id = self.model.get_category_id_by_name_test(category_name)
            date = datetime.strptime(
                self.view.budget_date_entry.get(), "%d-%m-%Y"
            ).date()
            budget_info = {
                "name_budget": name_budget,
                "initial_amount": initial_amount,
                "category_id": category_id,
                "date": date,
            }
            budget_id = self.model.create_budget_test(budget_info)
            if budget_id:
                self.view.budget_tree.insert(
                    "",
                    "end",
                    values=(name_budget, initial_amount, date, category_name),
                )
                self.view.budget_name_entry.delete(0, "end")
                self.view.budget_initial_amount_entry.delete(0, "end")
                self.view.budget_date_entry.delete(0, "end")
                self.view.budget_category_select.delete(0, "end")
                categories = self.model.list_categories_test()
                categories = [category[1] for category in categories]
                self.view.budget_category_select["values"] = categories
        else:
            self.view.budget_main_button.config(
                command=lambda: self.create_budget_controller("POST")
            )
            categories = self.model.list_categories_test()
            categories = [category[1] for category in categories]
            self.view.budget_category_select["values"] = categories
            self.view.create_budget_view()

    def expense_list_controller(self):
        """Method to list expenses"""
        expenses_list = self.model.list_expenses_test()
        self.view.expenses_list_view(expenses_list)

    def create_expense_controller(self, action="GET"):
        """Method to create an expense"""
        if action == "POST":
            name_expense = self.view.expense_name_entry.get()
            amount = self.view.expense_amount_entry.get()
            category_name = self.view.expense_category_select.get()
            category_id = self.model.get_category_id_by_name_test(category_name)
            date = datetime.strptime(
                self.view.expense_start_date_entry.get(), "%d-%m-%Y"
            ).date()
            budget_name = self.view.expense_budget_select.get()
            budget_id = self.model.get_budget_id_by_name_test(budget_name)
            expense_info = {
                "name_expense": name_expense,
                "amount": amount,
                "category_id": category_id,
                "start_date": date,
                "budget_id": budget_id,
            }
            expense_id = self.model.create_expense_test(expense_info)
            if expense_id:
                self.view.expense_tree.insert(
                    "",
                    "end",
                    values=(name_expense, amount, category_name),
                )
                self.view.expense_name_entry.delete(0, "end")
                self.view.expense_amount_entry.delete(0, "end")
                self.view.expense_category_select.delete(0, "end")
                categories = self.model.list_categories_test()
                categories = [category[1] for category in categories]
                self.view.expense_category_select["values"] = categories
        else:
            self.view.expense_main_button.config(
                command=lambda: self.create_expense_controller("POST")
            )
            categories = self.model.list_categories_test()
            categories = [category[1] for category in categories]
            self.view.expense_category_select["values"] = categories
            self.view.create_expense_view()


if __name__ == "__main__":
    TestController().run_test()
