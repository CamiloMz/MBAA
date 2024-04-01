""" View for the main page of the application. """

from tkinter import Tk, Button
from dataclasses import dataclass


@dataclass
class MainView:
    """Class for main view"""

    window = Tk()
    window.title("Monthly Budget and Analysis App")
    window.geometry("400x400")

    def run_view(self):
        """Method to run view"""
        self.window.mainloop()

    def list_options_view(self, options):
        """Method to list options"""
        for index, option in enumerate(options):
            button = Button(
                self.window,
                text=f"Manage {option.lower()}",
                width=20,
                height=2,
                bg="light blue",
                fg="black",
            )
            button.grid(row=index, column=0, padx=10, pady=10)
