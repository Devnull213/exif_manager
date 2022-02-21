#!/usr/bin/env python3

from custom_exceptions import NotValidExifInfo
import sys
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import time

class Manage_exif:

    replacement = {}

    def __init__(self, image: str):
        self.img_instance = Image.open(image)
    
    def is_exif_valid(self) -> Exception:
        nonetype = type(None)
        data = self.img_instance._getexif()
        if isinstance(data, nonetype) or len(data) <= 0:
            raise NotValidExifInfo(data)

    def get_exif(self) -> dict:
        data = self.img_instance._getexif()
        exif = {TAGS[key]:value for key, value in data.items() if key in TAGS}
        return exif 

    def get_gps_exif(self, exif: dict) -> dict:
        gps_data = exif['GPSInfo']
        gps_exif = {GPSTAGS[key]:value for key, value in gps_data.items() if key in GPSTAGS}
        return gps_exif

    def create_map_url(self, gps_info: dict) -> str:
        template = 'https://www.google.com/maps/?q='
        latitude = gps_info['GPSLatitude']
        longitude = gps_info['GPSLongitude']
        final_latitude = latitude[0] + (latitude[1]/60.0) + (latitude[2]/3600.0)
        final_longitude = longitude[0] + (longitude[1]/60.0) + (longitude[2]/3600.0)
        map_url = f'{template}{final_latitude},{final_longitude}'
        return map_url

    def get_report_exif_data(self, exif_info: dict, map_url: str ):
        data = ["Exif Data General Info"] 
        for key, value in exif_info.items():
            if key != 'MakerNote' and key != 'GPSInfo':
                data.append(f"{key}: {value}")
                report_data = '\n'.join(data)
        print(report_data)
        return report_data

    def default_info(self):
        data2 = self.img_instance
        print(data2.filename)
        print(data2.size)
        print(data2.mode)
        print(data2.format)
        image_attr = ['filename', 'format', 'mode', 'size', 'width', 'heigth' ]
        data = self.img_instance.__dict__
        # default_keywords = [ item for item in data.keys() ]
        # default_items = [ item for item in data.values() ]

        # for item in default_keywords:
            # print(data2.item)
        # print(default_keywords)
        # print(default_items)
            


    # def delete_exif(self, exif):
        # self.data = self.img_instance._getexif()
        # self.data = self.replacement
        # self.img_instance.save(sys.argv[1])
        # print(self.data)


    def end_img_instance(self):
        self.img_instance.close()
        print("closed")

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
    print("Welcome to the exif manager, please choose an option: \n")
    print("1) See exif info on terminal")
    print("2) Export exif info on txt")
    print("3) Delete exif info")
    print("4) Quit")

    manager = Manage_exif(sys.argv[1])
    manager.is_exif_valid()
    exif_info = manager.get_exif()
    for key in exif_info.keys():
        if key == 'GPSInfo':
            print("GPSSSSSSSSs")
            gps_info = manager.get_gps_exif(exif_info)
            map_url = manager.create_map_url(gps_info)
    manager.get_report_exif_data(exif_info, map_url)
    manager.default_info()

    # manager.delete_exif(exif)
    manager.end_img_instance()


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f'{__file__} took {elapsed} to run')




