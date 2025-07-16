from .exception import InvalidFinalStateException, InvalidInitialStateException
from .state import FSMState
from .types import Alphabet, FinalValue


class FiniteAutomation:
    def __init__(
        self,
        initial_state: FSMState,
        acceptable_final_states: set[FSMState] | None = None,
        acceptable_alphabets: set[Alphabet] | None = None,
    ) -> None:
        if not isinstance(initial_state, FSMState):
            raise InvalidInitialStateException(initial_state)
        self.state = initial_state
        self.acceptable_alphabets = acceptable_alphabets
        self.acceptable_final_states = acceptable_final_states 

    def is_acceptable_final_state(self, state: FSMState) -> bool:
        return state in self.acceptable_final_states
    
    def is_valid_input(self, _input: list[Alphabet]) -> bool:
        return all(char in self.acceptable_alphabets for char in _input)
    
    def run(self, _input: list[Alphabet]) -> FinalValue:
        for char in _input:
            self.state = self.state.next_state(char)

        if not self.is_acceptable_final_state(self.state):
            raise InvalidFinalStateException(
                self.state,
                self.acceptable_final_states,
            )
        return self.state.get_value()

