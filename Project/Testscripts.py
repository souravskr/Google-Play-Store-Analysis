import os
import sys
from Test_prep import add2nums, kagglekey, ckkaggle

def testvalkey():
    assert kagglekey() == True

def testvalkaggle():
    assert ckkaggle(0) == 1
