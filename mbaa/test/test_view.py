""" view for testing """

from tkinter import Tk, LabelFrame, ttk, Button, Entry, Label, StringVar
from tkcalendar import DateEntry
from dataclasses import dataclass


@dataclass
class TestView:
    """Class for test view"""

    # Constants
    WINDOW_WIDTH = 1130
    WINDOW_HEIGHT = 800
    CATEGORY_FRAME_HEIGHT = 420
    CATEGORY_FRAME_WIDTH = 280
    CATEGORY_TREE_WIDTH = 255
    CATEGORY_INPUT_WIDTH = 150
    CATEGORY_LABEL_WIDTH = 50
    CATEGORY_COLUMNS = ("Name", "Type")
    CATEGORY_TYPE = ["Pocket", "Expense", "Budget"]
    BUDGET_FRAME_WIDTH = 400
    BUDGET_FRAME_HEIGHT = 420
    BUDGET_INPUT_WIDTH = 150
    BUDGET_LABEL_WIDTH = 110
    BUDGET_COLUMNS = ("Name", "Initial Amount", "Final Amount")
    EXPENSE_FRAME_WIDTH = 400
    EXPENSE_FRAME_HEIGHT = 525
    EXPENSE_COLUMNS = (
        "Name",
        "Amount",
        "Ideal payment date",
        "Payment Date",
        "Recurring",
        "next payment date",
        "status",
    )
    BUTTON_WIDTH = 120

    edit_mode = False

    # Create the window
    window: Tk = Tk()
    window.title("Test View")
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # Create the label frames
    categories_tree_frame = LabelFrame(window, text="Categories")
    budget_tree_frame = LabelFrame(window, text="Budgets")
    expense_tree_frame = LabelFrame(window, text="Expenses")

    # Create the Treeview for each frame
    categories_tree = ttk.Treeview(
        categories_tree_frame, columns=CATEGORY_COLUMNS, show="headings", height=6
    )
    budget_tree = ttk.Treeview(
        budget_tree_frame, columns=CATEGORY_COLUMNS, show="headings", height=6
    )
    expense_tree = ttk.Treeview(
        expense_tree_frame, columns=EXPENSE_COLUMNS, show="headings", height=6
    )

    # Create the form label for each frame
    categories_form_label = Label(categories_tree_frame, text="Categories Form")
    budget_form_label = Label(budget_tree_frame, text="Budget Form")
    expense_form_label = Label(expense_tree_frame, text="Expense Form")

    # Create the labels, entries, comboboxes and buttons for categories
    category_name_label = Label(categories_tree_frame, text="Name:")
    category_name = StringVar()
    category_name_entry = Entry(categories_tree_frame, textvariable=category_name)
    category_type_label = Label(categories_tree_frame, text="Type:")
    category_type = StringVar()
    category_type_select = ttk.Combobox(
        categories_tree_frame,
        values=CATEGORY_TYPE,
        state="disabled",
        textvariable=category_type,
    )
    category_main_button = Button(
        categories_tree_frame, text="Create Category", state="disabled"
    )
    category_edit_button = Button(
        categories_tree_frame, text="Edit Category", state="disabled"
    )

    # Create the labels, entries, comboboxes and buttons for budgets
    budget_name_label = Label(budget_tree_frame, text="Name:")
    budget_name_entry = Entry(budget_tree_frame)
    budget_initial_amount_label = Label(budget_tree_frame, text="Initial Amount:")
    budget_initial_amount_entry = Entry(budget_tree_frame)
    budget_date_label = Label(budget_tree_frame, text="Date:")
    # budget_date_entry = Entry(budget_tree_frame)
    budget_category_label = Label(budget_tree_frame, text="Category:")
    budget_category_select = ttk.Combobox(budget_tree_frame, state="readonly")
    budget_main_button = Button(budget_tree_frame, text="Create Budget")
    budget_edit_button = Button(budget_tree_frame, text="Edit Budget")

    # Create a datepicker for the budget date
    budget_date_entry = DateEntry(
        budget_tree_frame,
        width=12,
        background="darkblue",
        date_pattern="MM-dd-yyyy",
        state="readonly",
    )

    # Create the labels, entries, comboboxes and buttons for expenses
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
    expense_is_recurrent_label = Label(expense_tree_frame, text="Is Recurrent:")
    expense_is_recurrent = StringVar()
    expense_is_recurrent_check = ttk.Checkbutton(
        expense_tree_frame,
        variable=expense_is_recurrent,
        onvalue="is_recurrent",
        offvalue="not_recurrent",
    )
    expense_last_payment_date_label = Label(
        expense_tree_frame, text="Last Payment Date:"
    )
    expense_last_payment_date_entry = DateEntry(
        expense_tree_frame,
        width=12,
        background="darkblue",
        date_pattern="MM-dd-yyyy",
        state="disabled",
    )
    expense_next_payment_date_label = Label(
        expense_tree_frame, text="Next Payment Date:"
    )
    expense_next_payment_date_entry = DateEntry(
        expense_tree_frame,
        width=12,
        background="darkblue",
        date_pattern="MM-dd-yyyy",
        state="disabled",
    )
    expense_main_button = Button(expense_tree_frame, text="Create Expense")
    expense_edit_button = Button(expense_tree_frame, text="Edit Expense")

    # Create a datepicker for the expense start date
    expense_start_date_entry = DateEntry(
        expense_tree_frame,
        width=12,
        background="darkblue",
        date_pattern="MM-dd-yyyy",
        state="readonly",
    )

    def run_view(self):
        """Method to run view"""
        self.window.mainloop()

    def categories_list_view(self, categories_list):
        """Method to list categories"""

        def category_selected(event):
            """Method to select a category"""
            if self.categories_tree.selection():
                self.edit_mode = True
                selected_item = self.categories_tree.selection()[0]
                category_name = self.categories_tree.item(selected_item)["values"][0]
                category_type = self.categories_tree.item(selected_item)["values"][1]
                self.category_name_entry.delete(0, "end")
                self.category_name_entry.insert(0, category_name)
                self.category_type_select.delete(0, "end")
                self.category_type_select.set(category_type)
                self.category_type_select.config(state="readonly")
                self.category_main_button.config(state="disabled")
                self.category_edit_button.config(state="normal")

        # Place the tree frame in the window
        self.categories_tree_frame.place(
            x=10,
            y=10,
            width=self.CATEGORY_FRAME_WIDTH,
            height=self.CATEGORY_FRAME_HEIGHT,
            anchor="nw",
        )

        # Structure columns
        self.categories_tree.column("Name", anchor="center", width=100)
        self.categories_tree.column("Type", anchor="center", width=100)

        # Create headings
        self.categories_tree.heading("Name", text="Name", anchor="center")
        self.categories_tree.heading("Type", text="Type", anchor="center")

        # Place the tree in the frame
        self.categories_tree.place(x=10, y=10, width=self.CATEGORY_TREE_WIDTH)

        # Insert values in the tree
        for category in categories_list:
            self.categories_tree.insert(
                "",
                "end",
                values=(category[1].capitalize(), category[2].capitalize()),
            )

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(
            self.categories_tree, orient="vertical", command=self.categories_tree.yview
        )
        scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")

        # Communicate the scrollbar with the tree
        self.categories_tree.configure(yscrollcommand=scrollbar.set)

        # add select function to the tree
        self.categories_tree.bind("<<TreeviewSelect>>", category_selected)

    def create_category_view(self):
        """Method to create a category"""

        def enable_select(value):
            """Method to enable the select"""
            if value == "0":
                self.category_type_select.config(state="disabled")
            if self.edit_mode is False:
                self.category_type_select.config(state="readonly")
                self.category_type_select.current(0)
            else:
                self.category_type_select.config(state="readonly")
            return True

        def enable_button(value):
            """Method to enable the button"""
            if value == "0":
                self.category_main_button.config(state="disabled")
            if self.edit_mode is False:
                self.category_main_button.config(state="normal")
            return True

        def clear_form():
            """Method to clear the form"""
            self.category_name_entry.delete(0, "end")
            self.category_type_select.delete(0, "end")
            self.category_type_select.current(0)
            self.category_type_select.config(state="disabled")
            self.category_main_button.config(state="disabled")
            self.category_edit_button.config(state="disabled")

        # Create the cancel button
        cancel_button = Button(self.categories_tree_frame, text="Cancel")
        # Register the commands for the validation
        validate_name_command = self.window.register(enable_select)
        # place the form components in the frame
        self.categories_form_label.place(x=10, y=210, width=240)
        self.category_name_label.place(x=10, y=240, width=self.CATEGORY_LABEL_WIDTH)
        self.category_name_entry.place(x=70, y=240, width=self.CATEGORY_INPUT_WIDTH)
        self.category_type_label.place(x=10, y=270, width=self.CATEGORY_LABEL_WIDTH)
        self.category_type_select.place(x=70, y=270, width=self.CATEGORY_INPUT_WIDTH)
        self.category_type_select.current(0)
        self.category_main_button.place(x=10, y=310, width=self.BUTTON_WIDTH)
        self.category_edit_button.place(x=145, y=310, width=self.BUTTON_WIDTH)
        cancel_button.place(x=80, y=350, width=self.BUTTON_WIDTH)
        # Validate the entry
        self.category_name_entry.config(
            validate="key", validatecommand=(validate_name_command, "%i")
        )
        # Enable the button
        self.category_type_select.bind("<<ComboboxSelected>>", enable_button)
        # Add cancel button command
        cancel_button.config(
            command=clear_form,
        )

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
                    expense[4],
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

        self.expense_is_recurrent_label.place(
            x=10,
            y=350,
            width=self.BUDGET_LABEL_WIDTH,
        )

        self.expense_is_recurrent_check.place(x=130, y=350)

        self.expense_last_payment_date_label.place(
            x=10,
            y=380,
            width=self.BUDGET_LABEL_WIDTH,
        )

        self.expense_last_payment_date_entry.place(
            x=130, y=380, width=self.BUDGET_INPUT_WIDTH
        )

        self.expense_next_payment_date_label.place(
            x=10,
            y=410,
            width=self.BUDGET_LABEL_WIDTH,
        )

        self.expense_next_payment_date_entry.place(
            x=130, y=410, width=self.BUDGET_INPUT_WIDTH
        )

        self.expense_main_button.place(x=10, y=440, width=self.BUTTON_WIDTH)

        self.expense_edit_button.place(x=140, y=440, width=self.BUTTON_WIDTH)

        cancel_button = Button(self.expense_tree_frame, text="Cancel")

        cancel_button.place(x=270, y=440, width=110)


if __name__ == "__main__":
    TestView().run_view()
