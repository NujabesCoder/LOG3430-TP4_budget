import os

os.system("git bisect start $badhash $goodhash")
os.system("git bisect run python managa.py test")