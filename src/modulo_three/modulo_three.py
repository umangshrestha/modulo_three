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

    def is_valid_alphabet(self, _input: str) -> bool:
        return _input in self.acceptable_alphabets

    def run(self, _input: str) -> FSMState:
        if not isinstance(_input, str) or not _input:
            raise InvalidAlphabetException(_input, 0)
        return super().run(_input)

    def reset_state(self) -> None:
        self.state = initial_state

    def __new__(cls, *args, **kwargs):
        """ Singleton pattern """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        else:
            cls._instance.reset_state()
        return cls._instance
