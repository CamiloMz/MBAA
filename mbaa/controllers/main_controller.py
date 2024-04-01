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
        self.list_options_controller()
        self.view.run_view()

    def list_options_controller(self):
        """Method to list options"""
        options = self.model.list_options()
        self.view.list_options_view(options)


if __name__ == "__main__":
    MainController().run_main_app()
