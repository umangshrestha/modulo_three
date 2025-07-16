from ..types import Alphabet
from .base_exception import BaseException


class InvalidInputException(BaseException):
    """Exception raised for invalid alphabet."""

    def __init__(self, _input: Alphabet, acceptable_alphabets: set[Alphabet]) -> None:
        message = (
            f'Invalid Input: "{_input}"\n'
            f"Only following alphabets are allowed: {', '.join(acceptable_alphabets)}"
        )
        super().__init__(message)
