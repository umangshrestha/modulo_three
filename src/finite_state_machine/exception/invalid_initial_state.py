from ..state import FSMState
from .base_exception import BaseException


class InvalidInitialStateException(BaseException):
    """Exception raised for invalid initial state."""

    def __init__(self, state: FSMState) -> None:
        message = (
            f"Invalid initial state: {state}\nInital state should implement FSMState"
        )
        super().__init__(message)
