from finite_state_machine.automation import FiniteAutomation
from finite_state_machine.exception import InvalidAlphabetException
from finite_state_machine.state import FSMState
from modulo_three.utils.state import Mod3State


class ModuloThree(FiniteAutomation):
    def __init__(self) -> None:
        super().__init__(Mod3State.S0)

    def is_valid_alphabet(self, _input: str) -> bool:
        return _input == '0' or _input == '1'

    def run(self, _input: str) -> FSMState:
        if not isinstance(_input, str):
            raise InvalidAlphabetException(_input, 0)
        return super().run(_input)
    