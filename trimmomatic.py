import subprocess
import os
# from upload_page_script import *

class Trimmomatic:
    """
    A class used to call trimmomatic.
    """
    def __init__(self, minlen, crop, file):
        """
        This function sets the default values for trimmomatic objects.
        """
        self.illuminaclip = "ILLUMINACLIP:TruSeq3-SE:2:30:10"
        self.leading = "LEADING:3"
        self.trailing = "TRAILING:3"
        self.minlen = "MINLEN:" + minlen
        self.crop = "CROP:" + crop
        self.filename = file

    def run_trimmomatic(self):
        """
        This function calls the tool trimmomatic and creates an output file in the specified place.
        """
        path_root = os.getcwd()
        path_trimmomatic = r"\tools\Trimmomatic-0.39"
        path_output = r"\trimmomatic_output"
    
        command = [
        "java", "-jar",
        path_root + r"\tools\Trimmomatic-0.39\trimmomatic-0.39.jar",
        "SE",
        path_root + r"\file_uploading" + "\\" + self.filename,
        path_root + path_output + r"\OUTPUT.fq",
        self.illuminaclip,
        self.leading,
        self.trailing,
        self.minlen,
        self.crop
        ]

        os.chdir(path_root + path_trimmomatic)
        subprocess.run(command)
        os.chdir(path_root)
