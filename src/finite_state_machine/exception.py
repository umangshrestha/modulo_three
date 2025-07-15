from typing import TypeVar

from .state import FSMState

T = TypeVar('T')


class BaseException(Exception):
    """ Base exception for the  Finite State Machine package. """
    pass



class InvalidTransitionException(BaseException):
    """ Exception raised for invalid transition. """
    def __init__(self, state: FSMState, _input: T) -> None:
        message = f"Invalid transition: {state} -> {_input}"
        super().__init__(message)