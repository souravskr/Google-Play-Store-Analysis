import os
import sys

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

def add2nums(x,y):
    try:
        z = int(x+y)
        return z
    except TypeError:
        print('Please use only integers')
