""" This module contains the CategoriesView class that is used to create the Categories view. """

from tkinter import ttk, Tk, LabelFrame
import mysql.connector
from mysql.connector import errorcode

# from models.categories_model import Categories
from controllers.categories_controller import CategoriesController
from utils.message import print_message


class CategoriesView:
    """Class to create the Categories view"""

    def __init__(self, window: Tk):
        self.root = window
        self.root.title("Categories")
        self.root.geometry("700x600")

        # Create a frame for the tree
        tree_frame = LabelFrame(self.root, text="Categories")
        tree_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Create the tree
        self.categories_tree = ttk.Treeview(tree_frame)
        self.categories_tree["columns"] = ("Name", "Description")
        self.categories_tree.column("#0", width=0, stretch="no")
        self.categories_tree.column("Name", anchor="w", width=200)
        self.categories_tree.column("Description", anchor="w", width=400)
        self.categories_tree.heading(
            "#0",
            text="",
            anchor="w",
        )
        self.categories_tree.heading("Name", text="Name", anchor="w")
        self.categories_tree.heading("Description", text="Description", anchor="w")
        self.categories_tree.pack(expand=True, fill="none", padx=10, pady=10)

        # create a frame for new category
        new_category_frame = LabelFrame(self.root, text="New Category")
        new_category_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Create the labels and entries for the new category
        name_label = ttk.Label(new_category_frame, text="Name")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(new_category_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        type_label = ttk.Label(new_category_frame, text="Type")
        type_label.grid(row=1, column=0, padx=10, pady=10)
        self.type_entry = ttk.Entry(new_category_frame)
        self.type_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create the buttons
        create_button = ttk.Button(
            new_category_frame,
            text="Create",
            command=self.create_category,
        )
        create_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # self.categories = Categories.get_all_categories()
        self.load_categories()

    def reset_fields(self):
        """Method to reset the fields"""
        self.name_entry.delete(0, "end")
        self.type_entry.delete(0, "end")

    def create_category(self):
        """Method to create a category"""
        try:
            CategoriesController.create_category(
                self.name_entry.get(), self.type_entry.get()
            )
            # self.categories = Categories.get_all_categories()
            self.load_categories()
            self.reset_fields()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print_message("Category already exists.", "warning")
            else:
                print_message(f"Error creating category: {error}", "error")

    def load_categories(self):
        """Method to load the categories into the tree"""
        # for category in self.categories:
        #     self.categories_tree.insert(
        #         "", "end", text=category[0], values=(category[1], category[2])
        #     )

    def run(self):
        """Method to run the Categories view"""
        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    view = CategoriesView(root)
    view.run()
