import logging 
logging.basicConfig(level=logging.INFO,format="%(asctime)s | %(levelname)-8s | %(funcName)s: %(message)s",
)
empty_selection_user_message:str = "You didn't select anything. Please enter a valid selection from the menu."
empty_selection_log:str = "Empty menu selection"

invalid_selection_message:str = "Your selection is not in the menu, please select a valid option from the displayed menu."
invalid_selection_log:str = "Invalid option selected: "

not_int_entered_message:str = "You did not enter a valid whole number! Please enter a valid whole number"
not_int_entered_log:str = "non int type entered where int is required"
def log_input_rejection(log_message:str,user_warning_message: str, value: str)->None:
    logging.warning(log_message,value)
    print(user_warning_message)
