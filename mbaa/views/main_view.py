""" Main application entry point. """

from tkinter import Tk, Label
from dataclasses import dataclass
from utils.constants import MAIN_VIEW_HEIGHT, MAIN_VIEW_TITLE, MAIN_VIEW_WIDTH

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


@dataclass
class MainView:
    """Class for main view"""

    # Create the window
    window: Tk = Tk()
    window.title(MAIN_VIEW_TITLE)
    window.geometry(f"{MAIN_VIEW_WIDTH}x{MAIN_VIEW_HEIGHT}")

    # Create the graph label
    label = Label(window, text="Budget Graph")

    def run_view(self):
        """Method to run view"""
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def on_closing(self):
        """Method to handle window closing"""
        plt.close("all")  # Close all Matplotlib figures
        self.window.quit()  # Quit the Tkinter main loop
        self.window.destroy()  # Destroy the Tkinter window

    def show_budget_graph_view(self, budget_data: dict):
        """Method to show budget graph"""
        self.label.pack()
        # DATA
        data_expenses_labels = []
        data_expenses_values = []
        for budget in budget_data:
            if len(budget["expenses"]) > 0:
                for expense in budget["expenses"]:
                    data_expenses_labels.append(expense["name"])
                    data_expenses_values.append(expense["amount"])
        fig, ax = plt.subplots()
        ax.pie(data_expenses_values, labels=data_expenses_labels, autopct="%1.1f%%")
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()


if __name__ == "__main__":
    MainView().run_view()
