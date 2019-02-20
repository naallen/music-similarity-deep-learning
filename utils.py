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

def set_logger(log_path):
    '''Sets a path for the logger
    
    Sets a path for the logger to save logfiles too. Anything logged will be printed to the console and the logfile, along with timestamps
    Code from CS230 code examples github
    
    Arguments:
      path {string} -- path to the log file to save to
    '''
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Logging to a file
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logger.addHandler(file_handler)

    # Logging to console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(stream_handler)
