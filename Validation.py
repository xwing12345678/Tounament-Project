#from typing import 
import logging
from logging_functs_and_config import log_input_rejection
def is_int(choice:str)->bool:
    result = False
    if not choice.strip().isdigit():
        return result
    result = True
    return result

def is_positive(integer:int)->bool:
        result = False
        if not integer > 0:
             return result
        result = True
        return result

def is_not_negative(integer:int)->bool:
    result = False
    if not integer >= 0:
            return result
    result = True
    return result

'''

def is_in_range(integer:int,start:int, finish:int )->bool:
    result = False
    valid_choices:list[int] = [choice for choice in range(start,finish)]
    if integer in valid_choices:
        result = True
    return result
    '''


empty_selection_user_message:str = "You didn't select anything. Please enter a valid selection from the menu."
empty_selection_log:str = "Empty menu selection%s"

invalid_selection_message:str = "Your selection is not in the menu, please select a valid option from the displayed menu."
invalid_selection_log:str = "Invalid option selected: %r"

def validate_menu_selection(menu_choices:list[str],message:str)->str:
    selection = ""
    while True:
        selection = input(message).lower().strip()
        if not selection:
            log_input_rejection(log_message=empty_selection_log,user_warning_message=empty_selection_user_message,value=selection)
            continue
        if selection not in menu_choices:
            log_input_rejection(invalid_selection_log,invalid_selection_message,selection)
            continue        
        return selection




