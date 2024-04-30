""" Model for main app"""

from dataclasses import dataclass
from models.budget_model import Budget
from models.categories_model import Categories
from models.expense_model import Expense


@dataclass
class MainModel:
    """Class for main model"""

    def get_budget_data(self):
        """Function to get budget data"""
        budgets = Budget().get_all_budgets()
        budgets_data = []
        for budget in budgets:
            budget_category = Categories().get_category_by_id(budget[4])
            budget_expenses = Expense().get_expenses_by_budget_id(budget[0])
            budget_expenses_view = []
            for expense in budget_expenses:
                budget_expenses_view.append(
                    {
                        "name": expense[0],
                        "amount": expense[1],
                        "category": expense[2],
                    }
                )
            budget_data = {
                "name": budget[1],
                "amount": budget[2],
                "category": budget_category[0][1],
                "expenses": budget_expenses_view,
            }

            budgets_data.append(budget_data)
        return budgets_data
