""" Model for main app"""

from dataclasses import dataclass


@dataclass
class MainModel:
    """Class for main model"""

    def list_options(self):
        """Method to list options"""
        options = ["Categories", "Budgets", "Expenses"]
        return options
