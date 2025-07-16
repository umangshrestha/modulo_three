import random
from typing import Callable

import pytest

from modulo_three import mod_three


def generate_binary_string(length: int) -> str:
    """Generate a random binary string of given length."""
    return "".join(random.choice("01") for _ in range(length))


def cheap_mod_three(binary_string: str) -> int:
    return int(binary_string, 2) % 3


@pytest.mark.parametrize("input_size", [10, 100, 1000, 10000])
def test_mod_three_benchmark(benchmark: Callable, input_size: int):
    """Benchmark ModuloThree implementation with different input sizes."""
    binary_string = generate_binary_string(input_size)
    
    result = benchmark(mod_three, binary_string)
    assert result == cheap_mod_three(binary_string)


@pytest.mark.parametrize("pattern,size", [
    ("alternating", 1000),  # 01010101...
    ("zeros", 1000),        # 000000...
    ("ones", 1000),         # 111111...
    ("random", 1000),       # Random mix
])
def test_mod_three_patterns(benchmark: Callable, pattern: str, size: int):
    """Benchmark ModuloThree implementation with different input patterns."""
    if pattern == "alternating":
        binary_string = "01" * (size // 2)
    elif pattern == "zeros":
        binary_string = "0" * size
    elif pattern == "ones":
        binary_string = "1" * size
    else:  # random
        binary_string = generate_binary_string(size)
    
    result = benchmark(mod_three, binary_string)
    assert result == cheap_mod_three(binary_string)


def test_mod_three_cached_transitions(benchmark: Callable):
    """Benchmark to verify caching effectiveness."""
    binary_string = "1010" * 250
    
    result = benchmark(mod_three, binary_string)
    assert result == cheap_mod_three(binary_string)


@pytest.mark.parametrize("input_string", [
    "1" * 100,
    "0" + "1" * 99, # Leading zero
    "1" + "0" * 99, # Leading one
])
def test_mod_three_edge_cases(benchmark: Callable, input_string: str):
    """Benchmark ModuloThree implementation with edge cases."""
    result = benchmark(mod_three, input_string)
    assert result == cheap_mod_three(input_string)