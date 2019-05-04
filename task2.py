import math
import signal
import time
from sys import exit

try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

try:
    import pygame
except ImportError:
    exit("This script requires the pygame module\nInstall with: sudo pip install pygame")

