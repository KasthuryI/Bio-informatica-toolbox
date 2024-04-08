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


@pytest.mark.parametrize('args, expected', [
    (("3", "3", "4:15", "10", "20", "examplefile.file"),
     [ "java", "-jar", r"{path_root}/tools/Trimmomatic-0.39/trimmomatic-0.39.jar",
        "SE", r"{path_root}/file_uploading/examplefile.file",
        r"{path_root}/{path_output}/OUTPUT.fq", "ILLUMINACLIP:TruSeq3-SE:2:30:10", "LEADING:3",
        "TRAILING:3", "SLIDINGWINDOW:4:15", "MINLEN:10", "CROP:20"]),
    (("3", "3", "4:15", "50", "25", "anotherexample.file"),

        [ "java", "-jar", r"{path_root}/tools/Trimmomatic-0.39/trimmomatic-0.39.jar",
        "SE", r"{path_root}/file_uploading/anotherexample.file",
        r"{path_root}/{path_output}/OUTPUT.fq", "ILLUMINACLIP:TruSeq3-SE:2:30:10", "LEADING:3",
        "TRAILING:3", "SLIDINGWINDOW:4:15", "MINLEN:50", "CROP:25"])
])
def test_command(args, expected):
    """
    This function tests the command_trimmomatic()
    function from the trimmomatic.py module.
    """
    path_root = os.getcwd()
    path_output = r"trimmomatic_output"

    test1 = Trimmomatic(*args)
    expected = [s.format(path_root=path_root, path_output=path_output) for s in expected]

    cmd = test1.command_trimmomatic()
    assert cmd == expected

