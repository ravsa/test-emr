print("HELLO WORLD")

from rudra import logger
from sys import argv
from json import loads

def load_hyper_params():
    """Load the hyper parameter from the command line args."""
    if len(argv) > 1:
        input_data = argv[1:]
        try:
            if input_data:
                return loads(input_data[0])
        except Exception as exc:
            logger.error("Unable to decode the hyper params")
            
print(load_hyper_params())
