import pygame
from pygame.locals import *
from mingus.core import notes, chords
from mingus.containers import *
from mingus.midi import fluidsynth
from os import sys
SF2 = 'soundfont.sf2'
OCTAVES = 5  # number of octaves to show
LOWEST = 2  # lowest octave to show
FADEOUT = 0.25  # coloration fadeout time (1 tick = 0.001)
WHITE_KEY = 0
BLACK_KEY = 1
WHITE_KEYS = [
    'C',
    'D',
    'E',
    'F',
    'G',
    'A',
    'B',
    ]
BLACK_KEYS = ['C#', 'D#', 'F#', 'G#', 'A#']