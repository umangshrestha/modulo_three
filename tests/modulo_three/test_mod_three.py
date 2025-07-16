import gc
import pytest
from sys import getsizeof

from finite_state_machine.exception import InvalidInputException
from modulo_three import mod_three
from modulo_three.modulo_three import ModuloThree
from modulo_three.state import Mod3State, TRANSITION_CACHE


def cheap_mod_three(binary_string: str) -> int:
    return int(binary_string, 2) % 3

@pytest.mark.parametrize("binary_string", [
    "0",
    "1",
    "00",
    "01",
    "10",
    "11",
    "000",
    "001",
    "010",
    "011",
    "100",
    "101",
    "110",
    "111",
    "0000001111111111111111111111111111111111111111111111111111111111",
    "11111111111111111111111111111111111111111111111111111111111011111",
])
def test_mod_three(binary_string: str):
    assert mod_three(binary_string) == cheap_mod_three(binary_string)

@pytest.mark.parametrize("binary_string", [
    "",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "11111111111111111111111111111111111111111111111111111111111011111 A",
    "APPLE",
    [],
    {},
    None,
    object(),
    lambda x: x,
    True,
    False,
    [1, 2, 3],
])
def test_mod_three_invalid_input(binary_string: str):
    with pytest.raises(InvalidInputException):
        mod_three(binary_string)

def test_singleton_pattern():
    instance1 = ModuloThree()
    instance2 = ModuloThree()
    assert instance1 is instance2

def test_state_reset_on_new_instance():
    instance1 = ModuloThree()
    instance1.process("1")
    instance2 = ModuloThree() 
    assert instance2.state == Mod3State.S0

def test_state_persistence():
    fsm = ModuloThree()
    
    fsm.process("1")
    assert fsm.state == Mod3State.S1
    
    fsm.process("1")
    assert fsm.state == Mod3State.S0

@pytest.mark.parametrize("binary_string", [
    "0" * 1000,  # 1000 zeros
    "1" * 1000,  # 1000 ones
    "01" * 500,  # Alternating 0,1
    "10" * 500,  # Alternating 1,0
])
def test_very_long_inputs(binary_string: str):
    """Test handling of very long input strings"""
    assert mod_three(binary_string) == cheap_mod_three(binary_string)

    