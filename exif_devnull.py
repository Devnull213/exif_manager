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
    print("Welcome to the exif manager, please choose an option:\n")
    print("1) View exif info on terminal")
    print("2) Export exif info on txt")
    print("3) Delete exif info")
    print("0) Quit")

    option = 100

    while option != 0:

        option = int(input("Enter option:\n"))
        time.sleep(0.3)
        assert option < 4, "The option is out of range"

        if option == 1:
            manager = Manage_exif(sys.argv[1])
            manager.is_exif_valid()
            exif_info = manager.get_exif()
            # for key in exif_info.keys():
                # if key == 'GPSInfo':
                    # print("GPSSSSSSSSs")
                    # gps_info = manager.get_gps_exif(exif_info)
                    # map_url = manager.create_map_url(gps_info)
            manager.get_report_exif_data(exif_info)
            manager.default_info()
            # manager.delete_exif(exif)
            manager.end_img_instance()
        elif option == 2:
            pass
        elif option == 3:
            pass

    time.sleep(0.3)
    print("Program finished.")

if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f'{__file__}, took {elapsed} to run.')
