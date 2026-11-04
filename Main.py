from Validation import validate_menu_selection
import logging
from program_data import teams,matches
from CRUD_functs import add_to_teams
placeholder = "Not implemented yet"
valid_choices:list[str] = [str(number)for number in range(1,12)]
valid_choice:bool = False
menu_message:str = """
                        ========== TOURNAMENT MANAGER ==========
                        1. Add team
                        2. Show all teams
                        3. Add match result
                        4. Show standings
                        5. Show leading team
                        6. Show best attacking team
                        7. Show team success rate
                        8. Show teams without wins
                        9. Show tournament summary
                        10. Check championship potential
                        11. Exit
                        Choose an option: 
                        """

def main():
    running:bool = True
    choice:str = ""   
    while running == True:
        choice = validate_menu_selection(valid_choices,menu_message)
        if choice == '1':
                add_to_teams()
            
        elif choice == '2':
                print(placeholder)

        elif choice == '3':
                print(placeholder)

        elif choice == '4':
                print(placeholder)

        elif choice == '5':
                print(placeholder)

        elif choice == '6':
                print(placeholder)

        elif choice == '7':
                print(placeholder)

        elif choice == '8':
                print(placeholder)

        elif choice == '9':
                print(placeholder)

        elif choice == '10':
                print(placeholder)
                                                                                    
        else:
            print("Thank you for using the Tournament manager!")
            print("Hope to see you again soon!")
            running = False
            break
        
                


            
        











if __name__ == "__main__": 
    main()
    