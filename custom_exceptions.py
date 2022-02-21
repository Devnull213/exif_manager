#!/usr/bin/env python3

class NotValidExifInfo(Exception):

    def __init__(self, exif_info, message="Exif info not valid"):
        self.exif_info = exif_info
        self.message = message
        super().__init__(self.message)


    
