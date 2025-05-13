import sys
from src.logger import logging #importing already-configured logging.

#Every log message you write will go to the same logs/*.log file with a consistent format, automatically.

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
    #If you didn’t pass sys, your CustomException wouldn’t be able to get the traceback info at the point the exception occurred — which is vital for debugging.
    # the sys module, which is used to access detailed info about the exception (like traceback, line number, file name).