#!/usr/bin/env python3

import sys
import time
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

    option = 100 

    manager = Manage_exif(sys.argv[1])
    main_data = manager.main_exec()

    print("""Welcome to the exif manager, please choose an option:\n
    1) View exif info on terminal\r
    2) Export exif info on txt\r
    3) Delete exif info\r
    0) Quit\n""")

    while option != 0:

        option = int(input("Enter option: "))
        time.sleep(0.3)

        if option == 1:
            print(main_data)
        elif option == 2:
            with open ("./report.txt", "w") as report:
                report.write(main_data)
            print("Report generated succesfully.")
        elif option == 3:
            pass

    time.sleep(0.3)
    print("Program finished.")

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__}, took {elapsed} to run.")
