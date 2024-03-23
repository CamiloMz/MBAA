""" view for testing """

from tkinter import Tk, LabelFrame, ttk, Button, Entry, Label
from dataclasses import dataclass


@dataclass
class TestView:
    """Class for test view"""

    window: Tk = Tk()
    window.title("Test View")
    window.geometry("720x800")

    categories_tree_frame = LabelFrame(window, text="Categories")
    categories_tree = ttk.Treeview(categories_tree_frame, height=8)
    categories_form_label = Label(categories_tree_frame, text="Categories Form")
    category_name_label = Label(categories_tree_frame, text="Name:")
    category_name_entry = Entry(categories_tree_frame)
    category_type_label = Label(categories_tree_frame, text="Type:")
    category_type_entry = Entry(categories_tree_frame)
    category_main_button = Button(categories_tree_frame, text="Create Category")

    budget_tree_frame = LabelFrame(window, text="Budgets")
    budget_tree = ttk.Treeview(budget_tree_frame, height=4)
    budget_form_label = Label(budget_tree_frame, text="Budget Form")
    budget_name_label = Label(budget_tree_frame, text="Name:")
    budget_name_entry = Entry(budget_tree_frame)
    budget_initial_amount_label = Label(budget_tree_frame, text="Initial Amount:")
    budget_initial_amount_entry = Entry(budget_tree_frame)
    budget_date_label = Label(budget_tree_frame, text="Date:")
    budget_date_entry = Entry(budget_tree_frame)
    budget_category_label = Label(budget_tree_frame, text="Category:")
    budget_category_entry = Entry(budget_tree_frame)
    budget_main_button = Button(budget_tree_frame, text="Create Budget")

    def run_view(self):
        """Method to run view"""
        self.window.mainloop()

    def categories_list_view(self, categories_list):
        """Method to list categories"""
        # Place the tree frame in the window
        self.categories_tree_frame.place(x=10, y=10, width=280, height=380)

        # Structure the tree
        self.categories_tree["columns"] = ("Name", "Description")
        self.categories_tree.column("#0", width=0, stretch="no")
        self.categories_tree.column("Name", anchor="w", width=80)
        self.categories_tree.column("Description", anchor="w", width=100)
        self.categories_tree.heading(
            "#0",
            text="",
            anchor="w",
        )
        self.categories_tree.heading("Name", text="Name", anchor="w")
        self.categories_tree.heading("Description", text="Description", anchor="w")
        self.categories_tree.place(x=25, y=10, width=220)
        for category in categories_list:
            self.categories_tree.insert(
                "",
                "end",
                values=(category[1], category[2]),
            )

    def create_category_view(self):
        """Method to create a category"""
        self.categories_form_label.place(x=10, y=220, width=280)
        self.category_name_label.place(x=10, y=250, width=50)
        self.category_name_entry.place(x=70, y=250, width=150)
        self.category_type_label.place(x=10, y=280, width=50)
        self.category_type_entry.place(x=70, y=280, width=150)
        self.category_main_button.place(x=20, y=320, width=110)
        cancel_button = Button(self.categories_tree_frame, text="Cancel")
        cancel_button.place(x=150, y=320, width=110)

    def budget_list_view(self, budget_list):
        """Method to list budgets"""
        # Create a frame for the tree
        self.budget_tree_frame.place(x=310, y=10, width=400, height=380)

        # Create the tree
        self.budget_tree["columns"] = (
            "Name",
            "Initial Amount",
            "Final Amount",
            "Date",
        )
        self.budget_tree.column("#0", width=0, stretch="no")
        self.budget_tree.column("Name", anchor="center", width=50)
        self.budget_tree.column("Initial Amount", anchor="center", width=100)
        self.budget_tree.column("Final Amount", anchor="center", width=100)
        self.budget_tree.column("Date", anchor="center", width=100)

        self.budget_tree.heading(
            "#0",
            text="",
            anchor="center",
        )
        self.budget_tree.heading("Name", text="Name", anchor="center")
        self.budget_tree.heading(
            "Initial Amount", text="Initial Amount", anchor="center"
        )
        self.budget_tree.heading("Final Amount", text="Final Amount", anchor="center")
        self.budget_tree.heading("Date", text="Date", anchor="center")
        self.budget_tree.place(x=10, y=10, width=360)
        for budget in budget_list:
            self.budget_tree.insert(
                "",
                "end",
                values=(budget[1], float(budget[2]), float(budget[3]), budget[4]),
            )

    def create_budget_view(self):
        """Method to create a budget"""
        self.budget_form_label.place(x=0, y=120, width=400)

        self.budget_name_label.place(x=10, y=150, width=110)
        self.budget_name_entry.place(x=130, y=150, width=180)

        self.budget_initial_amount_label.place(
            x=10,
            y=180,
            width=110,
        )
        self.budget_initial_amount_entry.place(x=130, y=180, width=180)

        self.budget_date_label.place(x=10, y=210, width=110)
        self.budget_date_entry.place(x=130, y=210, width=180)

        self.budget_category_label.place(x=10, y=240, width=110)
        self.budget_category_entry.place(x=130, y=240, width=180)

        self.budget_main_button.place(x=10, y=280, width=110)
        cancel_button = Button(self.budget_tree_frame, text="Cancel")
        cancel_button.place(x=150, y=280, width=110)


if __name__ == "__main__":
    TestView().run_view()
