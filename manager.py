#!/usr/bin/env python3
from custom_exceptions import NotValidExifInfo
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

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


    def get_report_exif_data(self, exif_info: dict) -> str:
        data = [f"{key}: {value}" for key, value in exif_info.items() if key != 'MakerNote' and key != 'GPSInfo']
        report_data = '\n'.join(data)
        return report_data

    def get_report_gps_data(self, gps_info: dict, url: str) -> str:
        data = [f"{key}: {value}" for key, value in gps_info.items()]
        report_data = '\n'.join(data)
        return report_data


    def default_info(self):
        # data2 = self.img_instance
        # print(data2.filename)
        # print(data2.format)
        # print(data2.mode)
        # print(data2.height)
        # print(data2.width)
        # image_attr = ['filename', 'format', 'mode', 'size', 'width', 'heigth' ]
        data = self.img_instance.__dict__

    def create_report_and_export(self, exif_data: str, gps_data=''):
        exif_banner = '''
======================================
========== EXIF INFORMATION ==========
======================================'''
        gps_banner = ('''
======================================
=========== GPS INFORMATION ==========                
======================================''')
        report_data = f'{exif_banner}\n{exif_data}\n{gps_banner}\n{gps_data}'
        with open ('./report.txt', 'w') as report:
            report.write(report_data)



    # def delete_exif(self, exif):
        # self.data = self.img_instance._getexif()
        # self.data = self.replacement
        # self.img_instance.save(sys.argv[1])
        # print(self.data)


    def end_img_instance(self):
        self.img_instance.close()
        print("closed")

