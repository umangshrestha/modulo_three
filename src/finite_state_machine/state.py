from enum import Enum
from typing import Self, TypeVar

T = TypeVar('T')


class FSMState(Enum): 
    """ Base class for all finite state machines. """

    def __str__(self) -> str:
        return self.name
    
    def next_state(self, _input: T) -> Self:
        raise NotImplementedError(f"next_state is not implemented for {self.__class__.__name__}")