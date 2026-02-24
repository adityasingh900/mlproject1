import sys 
from src.logger import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # Calls sys.exc_info(), which returns a tuple of three things: the Exception Type, the Exception Value, and the Traceback.
                                       # the "Traceback" object. Think of it as a map that points exactly to where the code crashed.
    
    file_name=exc_tb.tb_frame.f_code.co_filename  # to find the specific file name where the error happened
    error_message="Error is occcured in python script name[{0}] line number [{1}] error message [{2}] ".format(
        file_name,exc_tb.tb_lineno,str(error)

    )
    return error_message    
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    


if __name__ == "__main__":
    try:
        logging.info("Starting the division operation") # This will go to the file
        a = 1 / 0
    except Exception as e:
        # 1. Create the exception object
        custom_error = CustomException(e, sys)
        
        # 2. MANUALLY tell the logger to write this error to the file
        logging.error(custom_error.error_message)
        
        # 3. Raise the error so it still shows in your terminal
        raise custom_error