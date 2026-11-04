import logging 
logging.basicConfig(level=logging.INFO,format="%(asctime)s | %(levelname)-8s | %(funcName)s: %(message)s",
)

def log_input_rejection(log_message:str,user_warning_message: str, value: str)->None:
    logging.warning(log_message,value)
    print(user_warning_message)
