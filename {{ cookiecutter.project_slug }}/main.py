import logging

from dotenv import load_dotenv

from src.utils.my_logger import LoggerSetup

# Initialize logger setup
LoggerSetup()

# Load environment variables
load_dotenv()

LOGGER: logging.Logger = logging.getLogger("main")


def main():
    return True


if __name__ == "__main__":
    main()
