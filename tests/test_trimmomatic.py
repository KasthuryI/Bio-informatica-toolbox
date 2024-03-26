import pytest
from trimmomatic import Trimmomatic



def test_hello():
    test1 = Trimmomatic('10', '20', 'here')
    cmd = test1.command_trimmomatic()