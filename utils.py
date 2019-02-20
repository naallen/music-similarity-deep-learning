import logging
import json

def load_json(path):
    '''Loads a json file at path to a dict.
    
    Example:
    ```
    params = load_json("params.json")
    ```
    
    Arguments:
      path {string} -- the path to the json file
    '''
    with open(path, 'r') as f:
        return json.load(f)

def make_logger(name, log_path):
    '''Creates a new logger with the given name and path, and returns it
    
    Creates a new logger which writes to the name and path provided. Also returns the logger.
    Partially adapted from CS230 code examples on Github
    
    Arguments:
        name {str} -- name of the logger
        log_path {str} -- path of the log file to write to
    
    Returns:
        logger -- the created logger
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Logging to file
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logger.addHandler(file_handler)

    # Logging to console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(stream_handler)

    return logger

