from modulo_three.utils.state import Mod3State
from finite_state_machine.exception import InvalidTransitionException
import pytest

@pytest.mark.parametrize("state, expected", [
    (Mod3State.S0, 0),
    (Mod3State.S1, 1),
    (Mod3State.S2, 2),
])
def test_mod3_state_output_value(state: Mod3State, expected: int):
    assert state.value == expected


@pytest.mark.parametrize("state, input, expected", [
    (Mod3State.S0, '0', Mod3State.S0),
    (Mod3State.S0, '1', Mod3State.S1),
    (Mod3State.S1, '0', Mod3State.S2),
    (Mod3State.S1, '1', Mod3State.S0),
    (Mod3State.S2, '0', Mod3State.S1),
    (Mod3State.S2, '1', Mod3State.S2),
])
def test_mod3_state_next_state(state: Mod3State, input: str, expected: Mod3State):
    assert state.next_state(input) == expected


@pytest.mark.parametrize("state, input", [
    (Mod3State.S0, '2'),
    (Mod3State.S1, '2'),
    (Mod3State.S2, '2'),
])
def test_mod3_state_next_state_invalid_input(state: Mod3State, input: str):
    with pytest.raises(InvalidTransitionException):
        state.next_state(input)




