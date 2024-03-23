""" Module for pocket model """

from dataclasses import dataclass


@dataclass
class Pocket:
    """Class for pocket model"""

    id: str
    name: str
    amount: float
    description: str
