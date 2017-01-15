# py.test -s -v test.py
import pytest
from  md2text import convert

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_check_bold():
    # print(convert("***Hello world!***"))
    assert convert("* Bla-bla \n **Hello world!*** \n* 1)dsjdf") == "\n• Bla-bla \n Hello world! \n• 1)dsjdf"
    assert convert("***Hello world!*** \n**Hi! \n* 1) Something 1 \n* 2) Something 2 \n* 3) Something 3") == \
           "Hello world! \nHi! \n• 1) Something 1 \n• 2) Something 2 \n• 3) Something 3"
    assert convert("_**Hello world!_** \n~~Hi!~~ a~b > c \n> Something 1 \n >>Something 2 \n >Something 3") == \
           "Hello world! \nHi! a~b > c \n\t Something 1 \n\tSomething 2 \n\tSomething 3"
