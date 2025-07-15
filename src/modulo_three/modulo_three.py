from finite_state_machine.automation import FiniteAutomation
from finite_state_machine.exception import InvalidAlphabetException
from finite_state_machine.state import FSMState
from modulo_three.utils.state import Mod3State

initial_state = Mod3State.S0

class ModuloThree(FiniteAutomation):
    _instance = None

    def __init__(self) -> None:
        super().__init__(initial_state)


    def is_valid_alphabet(self, _input: str) -> bool:
        return _input == '0' or _input == '1'

    def run(self, _input: str) -> FSMState:
        if not isinstance(_input, str):
            raise InvalidAlphabetException(_input, 0)
        return super().run(_input)

    def __new__(cls, *args, **kwargs):
        """ Singleton pattern to ensure only one instance of the class is created. """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        else:
            cls._instance.state =  initial_state
        return cls._instance
