""" Module for test controller """

from dataclasses import dataclass
from test.test_model import TestModel
from test.test_view import TestView
from models.enums import CategoryType


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
        self.view.run_view()

    def categories_list_controller(self):
        """Method to list categories"""
        categories_list = self.model.list_categories_test()
        self.view.categories_list_view(categories_list)

    def create_category_controller(self, action="GET"):
        """Method to create a category"""
        if action == "POST":
            name_category = self.view.category_name_entry.get()
            category_type = self.view.category_type_entry.get()
            category_id = self.model.create_category_test(name_category, category_type)
            if category_id:
                self.view.categories_tree.insert(
                    "",
                    "end",
                    values=(name_category, category_type),
                )
                self.view.category_name_entry.delete(0, "end")
                self.view.category_type_entry.delete(0, "end")
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
            category_name = self.view.budget_category_entry.get()
            category_type = CategoryType.BUDGET.value
            budget_info = {
                "name_budget": name_budget,
                "initial_amount": initial_amount,
                "name_category": category_name,
                "category_type": category_type,
            }
            self.model.create_budget_test(budget_info)
        else:
            self.view.budget_main_button.config(
                command=lambda: self.create_budget_controller("POST")
            )
            self.view.create_budget_view()


if __name__ == "__main__":
    TestController().run_test()
