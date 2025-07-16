def remove_leading_zeros(_input: str) -> str:
    """Remove leading zeros as they don't affect the result."""
    trimmed = _input.lstrip("0")
    return trimmed if trimmed else "0"
