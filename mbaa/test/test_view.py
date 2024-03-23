""" view for testing """

from tkinter import Tk, LabelFrame, ttk, Button, Entry, Label
from dataclasses import dataclass


@dataclass
class TestView:
    """Class for test view"""

    WINDOW_WIDTH = 1130
    WINDOW_HEIGHT = 800
    CATEGORY_FRAME_HEIGHT = 420
    CATEGORY_FRAME_WIDTH = 280
    CATEGORY_TREE_WIDTH = 255
    BUDGET_FRAME_WIDTH = 400
    BUDGET_FRAME_HEIGHT = 420
    EXPENSE_FRAME_WIDTH = 400
    EXPENSE_FRAME_HEIGHT = 420
    CATEGORY_INPUT_WIDTH = 150
    CATEGORY_LABEL_WIDTH = 50
    BUDGET_INPUT_WIDTH = 150
    BUDGET_LABEL_WIDTH = 110
    BUTTON_WIDTH = 120
    CATEGORY_TYPE = ["-- select one --", "Pocket", "Expense", "Budget"]

    window: Tk = Tk()
    window.title("Test View")
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    categories_tree_frame = LabelFrame(window, text="Categories")
    categories_tree = ttk.Treeview(categories_tree_frame, height=8)
    categories_form_label = Label(categories_tree_frame, text="Categories Form")
    category_name_label = Label(categories_tree_frame, text="Name:")
    category_name_entry = Entry(categories_tree_frame)
    category_type_label = Label(categories_tree_frame, text="Type:")
    category_type_select = ttk.Combobox(
        categories_tree_frame, values=CATEGORY_TYPE, state="readonly"
    )
    category_main_button = Button(categories_tree_frame, text="Create Category")
    category_edit_button = Button(categories_tree_frame, text="Edit Category")

    budget_tree_frame = LabelFrame(window, text="Budgets")
    budget_tree = ttk.Treeview(budget_tree_frame, height=6)
    budget_form_label = Label(budget_tree_frame, text="Budget Form")
    budget_name_label = Label(budget_tree_frame, text="Name:")
    budget_name_entry = Entry(budget_tree_frame)
    budget_initial_amount_label = Label(budget_tree_frame, text="Initial Amount:")
    budget_initial_amount_entry = Entry(budget_tree_frame)
    budget_date_label = Label(budget_tree_frame, text="Date:")
    budget_date_entry = Entry(budget_tree_frame)
    budget_category_label = Label(budget_tree_frame, text="Category:")
    budget_category_select = ttk.Combobox(budget_tree_frame, state="readonly")
    budget_main_button = Button(budget_tree_frame, text="Create Budget")
    budget_edit_button = Button(budget_tree_frame, text="Edit Budget")

    expense_tree_frame = LabelFrame(window, text="Expenses")
    expense_tree = ttk.Treeview(expense_tree_frame, height=6)
    expense_form_label = Label(expense_tree_frame, text="Expense Form")
    expense_name_label = Label(expense_tree_frame, text="Name:")
    expense_name_entry = Entry(expense_tree_frame)
    expense_amount_label = Label(expense_tree_frame, text="Amount:")
    expense_amount_entry = Entry(expense_tree_frame)
    expense_start_date_label = Label(expense_tree_frame, text="Start Date:")
    expense_start_date_entry = Entry(expense_tree_frame)
    expense_budget_label = Label(expense_tree_frame, text="Budget:")
    expense_budget_select = ttk.Combobox(expense_tree_frame, state="readonly")
    expense_category_label = Label(expense_tree_frame, text="Category:")
    expense_category_select = ttk.Combobox(expense_tree_frame, state="readonly")
    expense_main_button = Button(expense_tree_frame, text="Create Expense")
    expense_edit_button = Button(expense_tree_frame, text="Edit Expense")

    def run_view(self):
        """Method to run view"""
        self.window.mainloop()

    def categories_list_view(self, categories_list):
        """Method to list categories"""
        # Place the tree frame in the window
        self.categories_tree_frame.place(
            x=10,
            y=10,
            width=self.CATEGORY_FRAME_WIDTH,
            height=self.CATEGORY_FRAME_HEIGHT,
            anchor="nw",
        )

        # Structure the tree
        self.categories_tree["columns"] = ("Name", "Description")
        self.categories_tree.column("#0", width=0, stretch="no")
        self.categories_tree.column("Name", anchor="center", width=100)
        self.categories_tree.column("Description", anchor="center", width=100)
        self.categories_tree.heading(
            "#0",
            text="",
            anchor="center",
        )
        self.categories_tree.heading("Name", text="Name", anchor="center")
        self.categories_tree.heading("Description", text="Description", anchor="center")
        self.categories_tree.place(x=10, y=10, width=self.CATEGORY_TREE_WIDTH)
        for category in categories_list:
            self.categories_tree.insert(
                "",
                "end",
                values=(category[1], category[2]),
            )

    def create_category_view(self):
        """Method to create a category"""
        self.categories_form_label.place(x=10, y=210, width=240)
        self.category_name_label.place(x=10, y=240, width=self.CATEGORY_LABEL_WIDTH)
        self.category_name_entry.place(x=70, y=240, width=self.CATEGORY_INPUT_WIDTH)
        self.category_type_label.place(x=10, y=270, width=self.CATEGORY_LABEL_WIDTH)
        self.category_type_select.place(x=70, y=270, width=self.CATEGORY_INPUT_WIDTH)
        self.category_main_button.place(x=10, y=310, width=self.BUTTON_WIDTH)
        self.category_edit_button.place(x=145, y=310, width=self.BUTTON_WIDTH)
        cancel_button = Button(self.categories_tree_frame, text="Cancel")
        cancel_button.place(x=80, y=350, width=self.BUTTON_WIDTH)

    def budget_list_view(self, budget_list):
        """Method to list budgets"""
        # Create a frame for the tree
        self.budget_tree_frame.place(
            x=310, y=10, width=self.BUDGET_FRAME_WIDTH, height=self.BUDGET_FRAME_HEIGHT
        )

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
        self.budget_form_label.place(x=0, y=170, width=400)

        self.budget_name_label.place(x=10, y=200, width=self.BUDGET_LABEL_WIDTH)
        self.budget_name_entry.place(x=130, y=200, width=self.BUDGET_INPUT_WIDTH)

        self.budget_initial_amount_label.place(
            x=10,
            y=230,
            width=self.BUDGET_LABEL_WIDTH,
        )
        self.budget_initial_amount_entry.place(
            x=130, y=230, width=self.BUDGET_INPUT_WIDTH
        )

        self.budget_date_label.place(x=10, y=260, width=self.BUDGET_LABEL_WIDTH)
        self.budget_date_entry.place(x=130, y=260, width=self.BUDGET_INPUT_WIDTH)

        self.budget_category_label.place(x=10, y=290, width=self.BUDGET_LABEL_WIDTH)
        self.budget_category_select.place(x=130, y=290, width=self.BUDGET_INPUT_WIDTH)

        self.budget_main_button.place(x=10, y=330, width=self.BUTTON_WIDTH)
        self.budget_edit_button.place(x=140, y=330, width=self.BUTTON_WIDTH)
        cancel_button = Button(self.budget_tree_frame, text="Cancel")
        cancel_button.place(x=270, y=330, width=110)

    def expenses_list_view(self, expenses_list):
        """Method to list expenses"""
        self.expense_tree_frame.place(
            x=720,
            y=10,
            width=self.EXPENSE_FRAME_WIDTH,
            height=self.EXPENSE_FRAME_HEIGHT,
        )

        self.expense_tree["columns"] = (
            "Name",
            "Amount",
            "Start Date",
            "End Date",
            "Category",
        )
        self.expense_tree.column("#0", width=0, stretch="no")
        self.expense_tree.column("Name", anchor="center", width=50)
        self.expense_tree.column("Amount", anchor="center", width=100)
        self.expense_tree.column("Start Date", anchor="center", width=100)
        self.expense_tree.column("Category", anchor="center", width=100)
        self.expense_tree.heading(
            "#0",
            text="",
            anchor="center",
        )
        self.expense_tree.heading("Name", text="Name", anchor="center")
        self.expense_tree.heading("Amount", text="Amount", anchor="center")
        self.expense_tree.heading("Start Date", text="Start Date", anchor="center")
        self.expense_tree.heading("End Date", text="End Date", anchor="center")
        self.expense_tree.heading("Category", text="Category", anchor="center")
        self.expense_tree.place(x=10, y=10, width=370)
        for expense in expenses_list:
            self.expense_tree.insert(
                "",
                "end",
                values=(
                    expense[1],
                    float(expense[2]),
                    expense[3],
                    expense[5],
                ),
            )

    def create_expense_view(self):
        """Method to create an expense"""
        self.expense_form_label.place(x=0, y=170, width=500)

        self.expense_name_label.place(x=10, y=200, width=self.BUDGET_LABEL_WIDTH)
        self.expense_name_entry.place(x=130, y=200, width=self.BUDGET_INPUT_WIDTH)

        self.expense_amount_label.place(x=10, y=230, width=self.BUDGET_LABEL_WIDTH)
        self.expense_amount_entry.place(x=130, y=230, width=self.BUDGET_INPUT_WIDTH)

        self.expense_start_date_label.place(
            x=10,
            y=260,
            width=self.BUDGET_LABEL_WIDTH,
        )
        self.expense_start_date_entry.place(x=130, y=260, width=self.BUDGET_INPUT_WIDTH)

        self.expense_budget_label.place(x=10, y=290, width=self.BUDGET_LABEL_WIDTH)
        self.expense_budget_select.place(x=130, y=290, width=self.BUDGET_INPUT_WIDTH)

        self.expense_category_label.place(x=10, y=320, width=self.BUDGET_LABEL_WIDTH)
        self.expense_category_select.place(x=130, y=320, width=self.BUDGET_INPUT_WIDTH)

        self.expense_main_button.place(x=10, y=360, width=self.BUTTON_WIDTH)
        self.expense_edit_button.place(x=140, y=360, width=self.BUTTON_WIDTH)
        cancel_button = Button(self.expense_tree_frame, text="Cancel")
        cancel_button.place(x=270, y=360, width=110)


if __name__ == "__main__":
    TestView().run_view()
