"""
Title: test_trimmomatic
Author: Mirte Draaijer, Ivar Lottman, Kasthury Inparajah, Storm Steller
Date: 1-4-2024
Version: 1.0
Summery: run trimmomatic test
"""
import pytest
import os
from trimmomatic import Trimmomatic


def test_command():
    """
    This function tests the command_trimmomatic()
    function from the trimmomatic.py module.
    """
    path_root = os.getcwd()
    path_output = r"/trimmomatic_output"

    test1 = Trimmomatic("3", "3", "4:15", "10", "20", "examplefile.file")
    test2 = Trimmomatic("3", "3", "4:15", "50", "25", "anotherexample.file")

    expected = [ "java", "-jar", path_root + r"/tools/Trimmomatic-0.39/trimmomatic-0.39.jar",
        "SE", path_root + r"/file_uploading" + "/" + test1.filename,
        path_root + path_output + r"/OUTPUT.fq", test1.illuminaclip, test1.leading,
        test1.trailing, test1.sliding, test1.minlen, test1.crop]

    expected2 = [ "java", "-jar", path_root + r"/tools/Trimmomatic-0.39/trimmomatic-0.39.jar",
        "SE", path_root + r"/file_uploading" + "/" + test2.filename,
        path_root + path_output + r"/OUTPUT.fq", test2.illuminaclip, test2.leading,
        test2.trailing, test2.sliding, test2.minlen, test2.crop]

    cmd = test1.command_trimmomatic()
    assert cmd == expected

    cmd2 = test2.command_trimmomatic()
    assert cmd2 == expected2
