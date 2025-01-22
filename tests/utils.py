# utils.py
import os
import sys
from functools import wraps
from logger import logger

# Define root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# Paths
BIN_DIR = os.path.join(ROOT_DIR, 'bin')
DATA_DIR = os.path.join(ROOT_DIR, 'data')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')

def log_function(func):
    """
    Decorator to log the start and completion of functions.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting function: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Completed function: {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Error in function {func.__name__}: {e}")
            raise

    return wrapper
