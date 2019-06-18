import os
import sys
from jitter import plot_jitter, read_file
from download import checkLicense 

def ckkaggle(a):
    try: 
        os.system('kaggle datasets download lava18/google-play-store-apps ')
        if os.path.isfile('./google-play-store-apps.zip'):
            return a + 1
    except Exception as e:
        print(e)

def kagglekey():
    try:
        home = os.environ['HOME']
        print(home)
        return os.path.isfile(home+'/.kaggle/kaggle.json')
    except Exception as e:
        print(e)

def testvalkey():
    assert kagglekey() == True

def testvalkaggle():
    assert ckkaggle(0) == 1

def testJitter():
    observed=plot_jitter(read_file('./Data/cleanData.csv'))
    expected=True
    assert observed == expected

def testLicense():
    observed = checkLicense()
    expected = True
    assert observed == expected

