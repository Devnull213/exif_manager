#!/usr/bin/env python3
from custom_exceptions import NotValidExifInfo
import os 
from PIL import Image 
from PIL.ExifTags import TAGS, GPSTAGS 
class Manage_exif:

    replacement = {'exif':'No data'}

    def __init__(self, image: str):
        self.image = image
        self.img_instance = Image.open(image)
    

    def is_exif_valid(self) -> None:
        nonetype = type(None)
        data = self.img_instance._getexif()
        if isinstance(data, nonetype) or len(data) <= 0:
            raise NotValidExifInfo(data)


    def get_exif(self) -> dict:
        data = self.img_instance._getexif()
        exif = {TAGS[key]:value for key, value in data.items() if key in TAGS}
        return exif 


    def get_gps_exif(self) -> dict:
        exif = self.get_exif()
        gps_data = exif["GPSInfo"]
        gps_exif = {GPSTAGS[key]:value for key, value in gps_data.items() if key in GPSTAGS}
        return gps_exif


    def create_map_url(self) -> str:
        gps_info = self.get_gps_exif()
        latitude = gps_info["GPSLatitude"]
        longitude = gps_info["GPSLongitude"]
        final_latitude = latitude[0] + (latitude[1]/60.0) + (latitude[2]/3600.0)
        final_longitude = longitude[0] + (longitude[1]/60.0) + (longitude[2]/3600.0)
        map_url = f"https://www.google.com/maps/?q={final_latitude},{final_longitude}"
        return map_url


    def get_report_exif_data(self) -> str:
        exif_info = self.get_exif()
        data = [f"{key}: {value}" for key, value in exif_info.items() if key != "MakerNote" and key != "GPSInfo"]
        report_data = '\n'.join(data)
        return report_data

    def get_report_gps_data(self) -> str:
        gps_info = self.get_gps_exif()
        data = [f"{key}: {value}" for key, value in gps_info.items()]
        report_data = '\n'.join(data)
        return report_data


    def report_format(self, reportexif):
        for item in reportexif:
            print(item)


    def default_info(self):
        # data2 = self.img_instance
        # print(data2.filename)
        pass

    def exif_report(self) -> None:
        exif_data = self.get_report_exif_data()
        exif_banner = """
======================================
========== EXIF INFORMATION ==========
======================================"""
        report_data = f"{exif_banner}\n{exif_data}\n"
        return report_data

    def gps_report(self) -> None:
        gps_data = self.get_report_gps_data()
        gps_banner = """
======================================
=========== GPS INFORMATION ==========                
======================================"""
        report_data = f"{gps_banner}\n{gps_data}\n"
        return report_data
    

    def show_data(self, exif_data, gps_data=''):
        print(exif_data)
        print(gps_data)


    def export(self):
        with open (f"./report.txt", 'w') as report:
            report.write(data)

    # def delete_exif(self, exif) -> None:
        # self.data = self.img_instance._getexif()
        # self.data = self.replacement
        # self.img_instance.save(sys.argv[1])
        # print(self.data)


    def end_img_instance(self) -> None:
        self.img_instance.close()
        print("closed")


    # Execution Cases

    def has_gps(self) -> list:
        data = self.get_exif()
        verification = [True for key in data.keys() if key == 'GPSInfo']
        return verification


    def normal_execution(self) -> str:
        self.get_exif()
        self.get_report_exif_data()
        data = self.exif_report()
        return data

    def with_gps(self) -> str:
        self.get_exif()
        self.get_gps_exif()
        self.create_map_url()
        self.get_report_exif_data()
        self.get_report_gps_data()
        exif = self.exif_report()
        gps = self.gps_report()
        data = exif + gps
        return data


    def main_exec(self) -> str:
        if len(self.has_gps()) > 0:
            return self.with_gps()
        else:
            return self.normal_execution()



