import pytest

from finite_state_machine.exception import InvalidAlphabetException
from modulo_three import mod_three


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
    with pytest.raises(InvalidAlphabetException):
        mod_three(binary_string)