"""
    Title: fastqc.py
    Author: Mirte Draaijer, Ivar Lottman, Kasthury Inparajah, Storm Steller
    Date: 25-3-2024
    Version: 1.0

    Summary: This program runs FastQC through the command line. This is done by using the terminal.
"""

import subprocess
import os
import sys


class class_fastqc:
    """
        Summary: Class used to call FastQC.

        This class has 1 method, the .run method. This method runs FastQC through the command line.
    """
    def __init__(self, filename):
        self.filename = filename
        self.path_root = os.getcwd()
        self.path_fastqc = r"/tools/FastQC"
        self.path_output = r"/static"

    def __str__(self):
        """
        This functioning prints that FastQC is running.

        : Param: None

        : Return: running trimmomatic printed to the terminal.
        """
        return ("Running FastQC")

    def run(self, input_folder):
        """
        This function runs FastQC through the command-line.

        Param:
            input_folder: The folder which contains the .fastq or .fq file.

        Return: None
        """

        # checking if OS is windows or linux
        if sys.platform.startswith('win'):
            command = ["java",
                "-Xmx250m",
                "-Dfastqc.unzip=true",
                "-Dfastqc.delete=true",
                # output location
                r"-Dfastqc.output_dir=" + self.path_root + self.path_output,
                "-classpath",
                ".;./sam-1.103.jar;./jbzip2-0.9.jar",
                "uk.ac.babraham.FastQC.FastQCApplication",
                # input file name and patn
                self.path_root + input_folder + "/" + self.filename]

        elif sys.platform.startswith('linux'):
            command = ["fastqc",
                       "--outdir",
                       # output location
                       self.path_root + self.path_output,
                       "--extract",
                       # input file name and path
                       self.path_root + input_folder + "/" + self.filename]

        # changes working folder to folder containing FastQC
        os.chdir(self.path_root + self.path_fastqc)
        subprocess.run(command)
        # changes working folder to the root
        os.chdir(self.path_root)
