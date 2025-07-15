from functools import lru_cache
from typing import Self

from typing_extensions import override

from finite_state_machine.exception import InvalidTransitionException
from finite_state_machine.state import FSMState


class Mod3State(FSMState):
  S0 = 0
  S1 = 1
  S2 = 2

  @override
  def get_value(self) -> int:
    return self.value

  @override
  def next_state(self, ch: str) -> Self:
    match (self, ch):
      case (Mod3State.S0, '0') | (Mod3State.S1, '1'):
        return Mod3State.S0
      case (Mod3State.S0, '1') | (Mod3State.S2, '0'):
        return Mod3State.S1
      case (Mod3State.S1, '0') | (Mod3State.S2, '1'):
        return Mod3State.S2
      case _:
        raise InvalidTransitionException(self, ch)

  @classmethod
  @lru_cache(maxsize=1)
  def get_all_possible_states(cls) -> set[Self]:
    return {member for member in cls.__members__.values()}
