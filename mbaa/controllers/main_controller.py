""" Controller for the main page """

from dataclasses import dataclass
from models.main_model import MainModel
from views.main_view import MainView


@dataclass
class MainController:
    """Class for main controller"""

    model = MainModel()
    view = MainView()

    def run_main_app(self):
        """Method to run main app"""
        self.show_budget_graph()
        self.view.run_view()

    def show_budget_graph(self):
        """Method to show budget graph"""
        budgets = self.model.get_budget_data()
        self.view.show_budget_graph_view(budgets)


if __name__ == "__main__":
    MainController().run_main_app()
