from enum import Enum
from typing import Self

from .types import Alphabet, FinalValue


class FSMState(Enum): 
    """ Base class for all finite state machines. """

    def __str__(self) -> str:
        return self.name
    
    def get_value(self) -> FinalValue:
        return self.value

    def next_state(self, _input: Alphabet) -> Self:
        class_name = self.__class__.__name__
        raise NotImplementedError(
            f"next_state is not implemented for {class_name}")
