# logger.py

from loguru import logger as loguru_logger
import logging
import os
import yaml
import sys

# Define root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
LOG_DIR = os.path.join(ROOT_DIR, 'logs')

# Path to config.yaml
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.yaml')

# Load config.yaml
def load_logging_config():
    default_logging_config = {
        'level': 'INFO',
        'log_format': 'standard',  # Options: 'standard', 'enhanced'
        'rotation': "5 MB",
        'retention': 5,  # Number of files to retain
        'to_console': True
    }

    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            try:
                config = yaml.safe_load(f)
                logging_config = config.get('logging', default_logging_config)
            except yaml.YAMLError as e:
                print(f"Error parsing config.yaml: {e}")
                logging_config = default_logging_config
    else:
        logging_config = default_logging_config

    return logging_config

# Initialize logging
def setup_logger():
    logging_config = load_logging_config()

    level = logging_config.get('level', 'INFO').upper()
    log_format_option = logging_config.get('log_format', 'standard')
    rotation = logging_config.get('rotation', "5 MB")
    retention = logging_config.get('retention', 5)
    to_console = logging_config.get('to_console', True)

    # Define log directory and file
    log_dir = os.path.join(ROOT_DIR, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'process.log')

    # Define log formats
    standard_format = (
        "{time:YYYY-MM-DD HH:mm:ss.SSS} [{level}] {message}"
    )

    enhanced_format = (
        "{time:YYYY-MM-DD HH:mm:ss.SSS} [{level}] [{module}] {message}"
    )

    # Select format based on configuration
    if log_format_option == 'enhanced':
        log_format = enhanced_format
    else:
        log_format = standard_format

    # Remove default Loguru handlers to prevent duplication
    loguru_logger.remove()

    # Add file handler
    loguru_logger.add(
        log_file,
        level=level,
        format=log_format,
        rotation=rotation,
        retention=retention,
        enqueue=True,  # To handle multi-threaded applications
        backtrace=True,
        diagnose=True
    )

    # Add console handler if enabled
    if to_console:
        loguru_logger.add(
            sys.stdout,
            level=level,
            format=log_format,
            colorize=True,
            enqueue=True,
            backtrace=True,
            diagnose=True
        )

    # Redirect standard logging to Loguru
    class InterceptHandler(logging.Handler):
        def emit(self, record):
            # Get corresponding Loguru level if it exists
            try:
                level = loguru_logger.level(record.levelname).name
            except ValueError:
                level = record.levelno

            # Find caller from where originated the logging call 
            frame, depth = logging.currentframe(), 2
            while frame and frame.f_code.co_filename == logging.__file__:
                frame = frame.f_back
                depth += 1

            # Bind script name
            script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
            loguru_logger.opt(depth=depth, exception=record.exc_info).bind(script_name=script_name).log(level, record.getMessage())

    logging.basicConfig(handlers=[InterceptHandler()], level=logging_config.get('level', 'INFO'), force=True)

# Setup the logger upon import
setup_logger()

# Expose Loguru's logger
logger = loguru_logger

__all__ = ['logger']
