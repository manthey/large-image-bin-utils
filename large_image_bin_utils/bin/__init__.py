import os
import sys


def program():
    path = os.path.join(os.path.dirname(__file__), os.path.basename(sys.argv[0]))
    os.execv(path, sys.argv)
