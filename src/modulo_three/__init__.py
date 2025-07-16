"""ModuloThree package.

This package provides a Finite State Automaton implementation for calculating
the remainder when dividing a binary number by 3.

Example:
    >>> from modulo_three import mod_three
    >>> mod_three("1101")  # 13 in decimal
    1
    >>> mod_three("1110")  # 14 in decimal
    2
    >>> mod_three("1111")  # 15 in decimal
    0
"""

from modulo_three.modulo_three import ModuloThree

__all__ = [
    "mod_three",
]


def mod_three(binary_string: str) -> int:
    """Calculate the remainder when dividing a binary number by 3."""
    modulo_three = ModuloThree()
    modulo_three.process(binary_string)
    return modulo_three.get_final_state()
