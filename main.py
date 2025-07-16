"""
This is a simple script to test the modulo three function.
"""
from modulo_three import mod_three
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


if __name__ == "__main__":
    _input = sys.argv[1]
    logger.info(f"User input: {_input}")
    try:
        mod_three = mod_three(_input)
        logger.info(f"Modulo three of {_input} is {mod_three}")
    except Exception as e:
        logger.error(f"Error: {e}")