from typing import override

from finite_state_machine.automation import FiniteAutomation
from finite_state_machine.exception import InvalidInputException
from modulo_three.state import Mod3State

initial_state = Mod3State.S0


class ModuloThree(FiniteAutomation):
    _instance = None

    def __init__(self) -> None:
        super().__init__(
            initial_state=initial_state,
            acceptable_alphabets={"0", "1"},
            acceptable_final_states=Mod3State.get_all_possible_states(),
        )

    @override
    def is_valid_input(self, _input: str) -> bool:
        return isinstance(_input, str) and _input and super().is_valid_input(_input)

    def reset_state(self) -> None:
        self.state = initial_state

    @staticmethod
    def remove_leading_zeros(_input: str) -> str:
        """Remove leading zeros as they don't affect the result."""
        trimmed = _input.lstrip("0")
        return trimmed if trimmed else "0"

    @override
    def process(self, _input: str) -> None:
        if not self.is_valid_input(_input):
            raise InvalidInputException(_input, self.acceptable_alphabets)

        self.state = self.state.next_state(_input)

    def __new__(cls, *args, **kwargs):
        """Singleton pattern"""
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        else:
            # Reset the state to the initial state
            cls._instance.reset_state()
        return cls._instance
