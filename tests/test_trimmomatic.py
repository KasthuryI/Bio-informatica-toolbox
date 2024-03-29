import pytest
import os
from trimmomatic import Trimmomatic



def test_command():
    """
    This function tests the command_trimmomatic() function from the trimmomatic.py module.
    """
    path_root = os.getcwd()
    path_output = r"\trimmomatic_output"

    test1 = Trimmomatic("10", "20", "examplefile.file")
    test2 = Trimmomatic("50", "25", "anotherexample.file")

    expected = ["java", "-jar", path_root + r"\tools\Trimmomatic-0.39\trimmomatic-0.39.jar", "SE",
    path_root + r"\file_uploading" + "\\" + test1.filename,
    path_root + path_output + r"\OUTPUT.fq",
    "ILLUMINACLIP:TruSeq3-SE:2:30:10", "LEADING:3", "TRAILING:3", test1.minlen, test1.crop]

    expected2 = ["java", "-jar", path_root + r"\tools\Trimmomatic-0.39\trimmomatic-0.39.jar", "SE",
    path_root + r"\file_uploading" + "\\" + test2.filename,
    path_root + path_output + r"\OUTPUT.fq",
    "ILLUMINACLIP:TruSeq3-SE:2:30:10", "LEADING:3", "TRAILING:3", test2.minlen, test2.crop]

    cmd = test1.command_trimmomatic()
    assert cmd == expected

    cmd2 = test2.command_trimmomatic()
    assert cmd2 == expected2
