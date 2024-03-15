"""Enums for the models"""

from enum import Enum


class BudgetCategoryId(Enum):
    """Enum for budget category types"""

    JOB = 1
    INCOME = 2
    SAVINGS = 3
    INVESTMENTS = 4
    DEBT = 5
    OTHER = 6
