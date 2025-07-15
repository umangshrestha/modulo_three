from .exception import InvalidAlphabetException, InvalidFinalStateException
from .state import FSMState
from .types import Alphabet, FinalValue


class FiniteAutomation:
    def __init__(
        self,
        initial_state: FSMState,
        acceptable_final_states: set[FSMState] | None = None,
        acceptable_alphabets: set[Alphabet] | None = None,
    ) -> None:
        self.state = initial_state
        self.acceptable_alphabets = acceptable_alphabets
        self.acceptable_final_states = acceptable_final_states 

    def is_acceptable_final_state(self, state: FSMState) -> bool:
        return state in self.acceptable_final_states
    
    def is_valid_alphabet(self, _input: Alphabet) -> bool:
        return _input in self.acceptable_alphabets
    
    def run(self, _input: list[Alphabet]) -> FinalValue:
        for i, char in enumerate(_input):
            if not self.is_valid_alphabet(char):
                raise InvalidAlphabetException(char, i)
            self.state = self.state.next_state(char)

        if not self.is_acceptable_final_state(self.state):
            raise InvalidFinalStateException(
                self.state,
                self.acceptable_final_states,
            )
        return self.state.get_value()

