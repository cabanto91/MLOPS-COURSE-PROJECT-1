from src.logger import get_logger
from src.custom_exception import CustomException


import sys


logger = get_logger(__name__)


def divide_number(a, b):
    try:
        result =  a / b
        logger.info(f"Divided {a} by {b} to get {result}")
        return result
    except Exception as e:
        logger.error(f"Division by zero error: {e}")
        raise CustomException("Division by zero is not allowed", sys)
    

if __name__ == "__main__":
    try:
        logger.info("Starting the division operation")
        divide_number(10, 2)
        divide_number(10, 0)
    except CustomException as ce:
        logger.error(f"Custom exception occurred: {ce}")
