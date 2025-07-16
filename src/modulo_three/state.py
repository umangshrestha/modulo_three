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
        """Input needs to be validated before calling this method."""
        cache_key = (self, ch)
        if result := TRANSITION_CACHE.get(cache_key):
            return result

        if not ch:
            raise InvalidTransitionException(self, ch)

        mid = len(ch) // 2
        first_half, second_half = ch[:mid], ch[mid:]

        intermediate = self.next_state(first_half)
        final_state = intermediate.next_state(second_half)
        TRANSITION_CACHE[cache_key] = final_state
        return final_state

    @classmethod
    @lru_cache(maxsize=1)
    def get_all_possible_states(cls) -> set[Self]:
        return {member for member in cls.__members__.values()}


# Pre-computed transitions for single-bit inputs
# Format: (current_state, input) -> next_state
TRANSITION_CACHE: dict[tuple[Mod3State, str], Mod3State] = {
    (Mod3State.S0, "0"): Mod3State.S0,
    (Mod3State.S0, "1"): Mod3State.S1,
    (Mod3State.S1, "1"): Mod3State.S0,
    (Mod3State.S1, "0"): Mod3State.S2,
    (Mod3State.S2, "1"): Mod3State.S2,
    (Mod3State.S2, "0"): Mod3State.S1,
}
