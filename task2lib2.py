import glob
import os
import re
import signal
import time
from sys import exit

try:
    import midi
    import midi.sequencer
except ImportError:
    exit("This script requires the midi module\nInstall with: sudo pip install midi")

try:
    import pygame
except ImportError:
    exit("This script requires the pygame module\nInstall with: sudo pip install pygame")

import pianohat