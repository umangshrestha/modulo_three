from typing import override

from finite_state_machine.automation import FiniteAutomation
from finite_state_machine.exception import InvalidAlphabetException
from finite_state_machine.state import FSMState
from modulo_three.state import Mod3State

initial_state = Mod3State.S0

class ModuloThree(FiniteAutomation):
    _instance = None

    def __init__(self) -> None:
        super().__init__(
            initial_state=initial_state,
            acceptable_alphabets={'0', '1'},
            acceptable_final_states=Mod3State.get_all_possible_states()
        )

    @override
    def is_valid_input(self, _input: str) -> bool:
        return (
            isinstance(_input, str)
            and _input 
            and all(char in self.acceptable_alphabets for char in _input)
        )

    def reset_state(self) -> None:
        self.state = initial_state

    @override
    def run(self, _input: str) -> FSMState:
        if not self.is_valid_input(_input):
            raise InvalidAlphabetException(_input, 0)
        _input = self.remove_trailing_zeros(_input)
        return super().run(_input)


    def remove_trailing_zeros(self, _input: str) -> str:
        return _input.lstrip('0')

    def __new__(cls, *args, **kwargs):
        """ Singleton pattern """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        else:
            # Reset the state to the initial state
            cls._instance.reset_state()
        return cls._instance
