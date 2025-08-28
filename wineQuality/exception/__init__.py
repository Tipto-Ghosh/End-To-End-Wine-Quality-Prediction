import sys 
from wineQuality.logger import logging

# define the error message
def error_message_format(error , error_details) -> str: 
    """ 
    Creates a detailed error message with file name, line number, and the actual error message.
    """ 
    _ , _ , exception_traceback = error_details.exc_info()
    file_name = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    
    return f"Error occurred in python script name [{file_name}] at line: [{line_number}] with error message [{str(error)}]"


class WineException(Exception): 
    def __init__(self, error , error_details):
        # make the error message format
        self.error_message = error_message_format(
            error = error , error_details = error_details
        )
        super().__init__(self.error_message)
        logging.error(self.error_message , exc_info = True)
    
    def __str__(self):
        return self.error_message