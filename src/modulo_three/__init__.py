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


def mod_three(binary_string: str) -> int:
    return ModuloThree().run(binary_string)


__version__ = "0.1.0" 