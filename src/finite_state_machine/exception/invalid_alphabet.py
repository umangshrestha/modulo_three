from ..types import Alphabet
from .base_exception import BaseException


class InvalidAlphabetException(BaseException):
    """ Exception raised for invalid alphabet. """
    def __init__(self, _input: Alphabet, position: int) -> None:
        message = f"Invalid alphabet: {_input} at position {position}"
        super().__init__(message)