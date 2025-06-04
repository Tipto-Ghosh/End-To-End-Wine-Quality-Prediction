import os 
import sys
import logging

# Define the log message format
logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s]"

# Define the log directory and log file path
log_dir = "logs"
log_filepath = os.path.join(log_dir , "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir , exist_ok = True)

# Set up basic configuration for logging
logging.basicConfig(
    level = logging.INFO, # Set logging level to INFO
    format = logging_str,  # Use the defined log message format
    
    handlers = [
        logging.FileHandler(log_filepath), # Log messages to a file
        logging.StreamHandler(sys.stdout)  # Also display logs in the console (stdout)
    ]
)

# Create a named logger instance (can be reused across modules)
logger = logging.getLogger("wineQualityLogger")