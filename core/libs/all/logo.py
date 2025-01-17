#!/usr/bin/env python3
__author__ = 'Khaled Nassar'
__email__ = 'knassar702@gmail.com'
__version__ = '0.7#Beta'

from datetime import datetime
from glob import glob
from .colors import dump_colors
import random
def logo():
    logos = []
    for logo in glob('conf/logo/*.txt'):
        logos.append(open(logo,'r').read().format(**dump_colors())) 
    print(random.choice(logos))

