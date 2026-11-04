from Validation import validate_menu_selection
from logging import* # type: ignore
valid_choices:list[str] = [str(number)for number in range(0,11)]
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
                        0. Exit
                        Choose an option: 
                        """

def main():
    running:bool = True    
    while running == True:
        choice:str = ""
        while main:
            choice = validate_menu_selection(valid_choices,menu_message)
        if choice == '0':
            pass
        elif choice == '1':
            pass
        elif choice == '1':
                    pass 
        elif choice == '1':
                    pass
        elif choice == '1':
                    pass
        elif choice == '1':
                    pass
        elif choice == '10':
                    pass
        else:
            print("Sorry I ran out of time")
                


            
        











if __name__ == "__main__": 
    main()
    