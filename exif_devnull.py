#!/usr/bin/env python3

import sys
from manager import Manage_exif

def main():

    print("""
 _______          _________ _______    ______   _______           _                 _        _       
(  ____ \|\     /|\__   __/(  ____ \  (  __  \ (  ____ \|\     /|( (    /||\     /|( \      ( \      
| (    \/( \   / )   ) (   | (    \/  | (  \  )| (    \/| )   ( ||  \  ( || )   ( || (      | (      
| (__     \ (_) /    | |   | (__      | |   ) || (__    | |   | ||   \ | || |   | || |      | |      
|  __)     ) _ (     | |   |  __)     | |   | ||  __)   ( (   ) )| (\ \) || |   | || |      | |      
| (       / ( ) \    | |   | (        | |   ) || (       \ \_/ / | | \   || |   | || |      | |      
| (____/\( /   \ )___) (___| )        | (__/  )| (____/\  \   /  | )  \  || (___) || (____/\| (____/\ 
(_______/|/     \|\_______/|/         (______/ (_______/   \_/   |/    )_)(_______)(_______/(_______/

                """)

    manager = Manage_exif(sys.argv[1])
    main_data = manager.main_exec()

    print("""Welcome to the exif manager, please choose an option:\n
    1) View exif info on terminal\r
    2) Export exif info on txt\r
    3) Delete exif info\r
    0) Quit\n""")

    while True:

        try:
            option = int(input("Enter option: "))

            if option == 1:
                print(main_data)

            elif option == 2:
                with open ("./report.txt", "w") as report:
                    report.write(main_data)
                print("Report generated succesfully.\n")

            elif option == 3:
                manager.delete_exif()

            elif option > 3:
                print("Option out of bounds, please choose again.")

            else:
                break

        except:
            print("You entered a non valid option, try again.")

    manager.end_img_instance()
    print("Program finished.")

if __name__ == "__main__":
    main()
