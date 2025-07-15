from ..state import FSMState
from .base_exception import BaseException


class InvalidFinalStateException(BaseException):
    """ Exception raised for invalid final state. """
    def __init__(self, state: FSMState, acceptable_final_states: list[FSMState]) -> None:
        message = f"Invalid final state: {state}\nAcceptable final states: {acceptable_final_states}"
        super().__init__(message)
