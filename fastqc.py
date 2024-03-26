"""
    Title: fastqc.py
    Author: Mirte Draaier, Ivar Lotman, Kasthury Imparajah, Storm Steller
    Date: 25-3-2024
    Summary: This programm runs FastQC through the terminal. It is meant to work for the Trimmtech website.
"""

import subprocess
import os

class class_fastqc:
    def __init__(self, filename):
        self.filename = filename
        self.path_root = os.getcwd()
        self.path_fastqc = r"\tools\FastQC"
        self.path_output = r"\static"

    def run(self, input_folder):
        """
        This function runs the programm with a pre-determined path, except for the filename.
        """
        command = ["java", 
                "-Xmx250m", 
                "-Dfastqc.unzip=true", 
                "-Dfastqc.delete=true", 
                r"-Dfastqc.output_dir=" + self.path_root + self.path_output,
                "-classpath", 
                ".;./sam-1.103.jar;./jbzip2-0.9.jar", 
                "uk.ac.babraham.FastQC.FastQCApplication",  
                self.path_root + input_folder + "\\" + self.filename]
        
        os.chdir(self.path_root + self.path_fastqc)
        subprocess.run(command)
        os.chdir(self.path_root)
