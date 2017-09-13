#!/usr/bin/env python

# This script merge head of *.po files back to Crowdin generated *.po files

# $1 is the po from SVN, with head info
# $2 is the po from Crowdin, without head info
# $3 is the output po file

import sys
import re

with open(sys.argv[1], 'r') as f:
    source_lines = f.readlines()

with open(sys.argv[2], 'r') as f:
    crowdin_contents = f.read()


# Read old credits

credits = ''

for line in source_lines:
    if line.startswith('#'):
        credits += line
    else:
        break

with open(sys.argv[2], 'w') as f:
    f.write(credits + crowdin_contents)
