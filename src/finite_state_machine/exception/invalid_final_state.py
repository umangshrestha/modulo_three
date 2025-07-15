from ..state import FSMState
from .base_exception import BaseException


class InvalidFinalStateException(BaseException):
    """ Exception raised for invalid final state. """
    def __init__(self,
        state: FSMState,
        acceptable_final_states: list[FSMState],
        acceptable_alphabets: list[str]
    ) -> None:
        message = f"Invalid final state: {state}\n"
        message += f"Acceptable final states: {acceptable_final_states}"
        super().__init__(message)
