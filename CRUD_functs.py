from program_data import teams,matches
from Validation import is_non_negative_int,list_has_duplicate_team,validate_empty_string_selection,log_input_rejection,is_positive,validate_empty_string_selection
import logging
from logging_functs_and_config import log_input_rejection,empty_selection_user_message,not_int_entered_message,not_int_entered_log

def create_team(id:int,name:str,)->dict[str,str|int]:
    new_team = {}
    new_team = {"id":id,"name":name,"played": 0,"wins": 0, "draws": 0, "losses": 0,
                                   "goals_for": 0, "goals_against": 0, "points": 0}
    return new_team

new_team_name_message = "Enter in the name of your new team. Make sure you enter something and that you don't take the name of another team"
new_team_id_message = "Enter in the id of your new team. Make sure you enter something and that you don't take the id of another team"

def input_valid_positive_int()->int:
    raw_selection = ""
    while True:
        raw_selection = input("Enter team ID (positive integer): ").strip()
        if not is_non_negative_int(raw_selection):
             log_input_rejection("Invalid ID entered: %s", "Error: ID must be a valid integer.", raw_selection)
             continue
        team_id_candidate:int = int(raw_selection)
                
        if not is_positive(team_id_candidate):
            log_input_rejection("Non-positive ID entered: %s", "Error: ID must be greater than 0.", raw_selection)
            continue
        team_id = team_id_candidate    
        return team_id

def input_team_name() -> str:
    while True:
        name:str = validate_empty_string_selection("Enter team name: ")           
        return name
    
def add_to_teams()->dict[str,str|int]:
    while True:
        team_id:int = input_valid_positive_int()
        team_name:str = input_team_name()   
        candidate_new_team = create_team(team_id,team_name)
        if teams:
            if list_has_duplicate_team(team_list=teams,new_team=candidate_new_team):
                log_input_rejection("Attempted duplicate team",
                                    "Warning the team you tried to enter already has a duplicate name or id in teams!  ",
                                      f' team id:{str(team_id)}, team name:{team_name}')
                continue
            new_team = candidate_new_team
        new_team = candidate_new_team    
        teams.append(new_team)
        return new_team

