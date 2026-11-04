#from typing import 
import logging
from logging_functs_and_config import log_input_rejection,empty_selection_log,empty_selection_user_message,invalid_selection_log,invalid_selection_message

def is_non_negative_int(choice:str)->bool:
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


 

def is_team_equal(team_dict1:dict[str,str|int],team_dict2:dict[str,str|int])->bool:
     result:bool = False
     if team_dict1["id"] == team_dict2["id"] or team_dict1["name"] == team_dict2["name"]:
        result = True
     return result

def list_has_duplicate_team(new_team:dict[str,str|int],team_list:list[dict[str,str|int]])->bool:
        result:bool = False
        for team in team_list:
            if is_team_equal(new_team,team):
                result = True
                return result
        return result

def validate_empty_string_selection(message:str ="Enter a non empty string")->str:
    selection = ""
    while True:
        selection = input(message).strip()
        if not selection:
            log_input_rejection(log_message=empty_selection_log,user_warning_message=empty_selection_user_message,value=selection)
            continue
        return selection
    
def validate_menu_selection(menu_choices:list[str],message:str)->str:
    selection = ""
    while True:
        selection = validate_empty_string_selection(message)
        if selection.lower() not in menu_choices:
            log_input_rejection(invalid_selection_log,invalid_selection_message,selection)
            continue        
        return selection


