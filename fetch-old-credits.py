#!/usr/bin/env python

# This script merge head of *.po files back to Crowdin generated *.po files

# $1 is the source file with credits
# $2 is the target file without credits

import sys
import re

with open(sys.argv[1], 'r') as f:
    source_lines = f.readlines()

with open(sys.argv[2], 'r') as f:
    target_lines = f.readlines()

# Read old credits

credits = ''
content = ''

for line in source_lines:
    if line.startswith('#'):
        credits += line
    else:
        break

content_start = False
for line in target_lines:
    if content_start:
        content += line
    elif line.startswith('msgid'):
        content_start = True
        content += line

with open(sys.argv[2], 'w') as f:
    f.write(credits + content)
