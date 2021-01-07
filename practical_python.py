from loguru import logger
import sys
import numpy as np
import pandas as pd
import yaml

logger.add("application.log", format="{time} {level} {message}", level="INFO")


def do_something(x):
    """
    This function does something.
    Args :
        x: Argument to do something.
    Returns :
        x: Returns the variable.
    """
    return (
        x
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
        + 1
    )


def read_config(path="config.yaml"):
    """
    Method to read the configutation file.
    Args :
        path : Path to the confi file.
    Returns :
        configuration : Dictionary of for configuration file.

    """
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


config = read_config()

logger.info(f"Starting code execution for project {config['project_name']}")
print(do_something(30))
logger.info("Code execution completed.")
