"""
A module containing class used to run the tool trimmomatic. 
"""

import subprocess
import os

class Trimmomatic:
    """
    A class used to call trimmomatic.
    """
    def __init__(self, minlen, crop, file):
        """
        This function sets the default values for trimmomatic objects.

        : Param minlen: the user input for the minimum length.
        : Param crop: the user input for the crop values.
        : Param file: the uploaded file.

        : Return: -
        """
        self.illuminaclip = "ILLUMINACLIP:TruSeq3-SE:2:30:10"
        self.leading = "LEADING:3"
        self.trailing = "TRAILING:3"
        self.minlen = "MINLEN:" + minlen
        self.crop = "CROP:" + crop
        self.filename = file

    def run_trimmomatic(self):
        """
        This function runs the tool trimmomatic and creates an output file in the specified place.

        : Param: -

        : Return: -
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

def __str__(self):
    """
    This functioning prints that trimmomatic is running.
    
    : Param: -
    
    : Return: running trimmomatic printed to the terminal.
    """
    return ("Running trimmomatic")