"""
A module containing class used to run the tool trimmomatic. 
"""

import subprocess
import os

class Trimmomatic:
    """
    A class used to call trimmomatic.

    command_trimmomatic(): generates the command used to run trimmomatic.
    run_trimmomatic(): runs the tool trimmomatic.
    """
    def __init__(self, sliding, minlen, crop, file):
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
        self.sliding = "SLIDINGWINDOW:" + str(sliding)
        self.minlen = "MINLEN:" + str(minlen)
        self.crop = "CROP:" + str(crop)
        self.filename = file

    def command_trimmomatic(self):
        """
        This funciton creates the command that is used to run trimmomatic.

        : Param: -

        : Return: a list containing the command.
        """
        path_root = os.getcwd()
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
        self.sliding,
        self.minlen,
        self.crop
        ]

        return command

    def run_trimmomatic(self):
        """
        This functions runs trimmomatic.

        : Param: -
        
        : Return: -
        """
        path_root = os.getcwd()
        path_trimmomatic = r"\tools\Trimmomatic-0.39"
        command = self.command_trimmomatic()

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
