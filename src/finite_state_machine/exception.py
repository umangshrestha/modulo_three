
from .state import FSMState
from .types import Alphabet


class BaseException(Exception):
    """ Base exception for the  Finite State Machine package. """
    pass


class InvalidTransitionException(BaseException):
    """ Exception raised for invalid transition. """
    def __init__(self, state: FSMState, _input: Alphabet) -> None:
        message = f"Invalid transition: {state} -> {_input}"
        super().__init__(message)


class InvalidFinalStateException(BaseException):
    """ Exception raised for invalid final state. """
    def __init__(self, state: FSMState, acceptable_final_states: list[FSMState]) -> None:
        message = f"Invalid final state: {state}\nAcceptable final states: {acceptable_final_states}"
        super().__init__(message)


class InvalidAlphabetException(BaseException):
    """ Exception raised for invalid alphabet. """
    def __init__(self, _input: Alphabet, position: int) -> None:
        message = f"Invalid alphabet: {_input} at position {position}"
        super().__init__(message)