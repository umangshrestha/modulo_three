from ..state import FSMState
from ..types import Alphabet
from .base_exception import BaseException


class InvalidTransitionException(BaseException):
    """ Exception raised for invalid transition. """
    def __init__(self, state: FSMState, _input: Alphabet) -> None:
        message = f"Invalid transition: {state} -> {_input}"
        super().__init__(message)
