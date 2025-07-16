"""List of generic types for the finite state machine package."""

from typing import TypeVar

Alphabet = TypeVar("Alphabet", bound=str)
FinalValue = TypeVar("FinalValue", bound=int)
