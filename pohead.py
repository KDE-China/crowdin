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

# Replace Crowdin username with real name

names = {
    "guoyunhebrave": "Guo Yunhe",
    "csslayer": "Weng Xuetian",
    "073plan": "Boyuan Yang",
    "henryhu": "Henry Hu",
    "xiangzhai83": "Leslie Zhai",
}

# Read new translator

m = re.search('Last-Translator: ([\-a-z0-9_]+) <([\.\-a-z0-9_]+@[\.\-a-z0-9]+)>', crowdin_contents)

name = m.group(1)
email = m.group(2)

m = re.search('PO-Revision-Date: (\d{4})', crowdin_contents)

year = m.group(1)

name = names.get(name, name)

m = re.search('# ' + name + ' <([\.\-a-z0-9_]+@[\.\-a-z0-9]+)>, [0-9,\. ]+', credits)

if m:
    line = m.group(0)
    years = re.findall('\d{4}', line)
    if not year in years:
        years.append(year)
    new_line = '# ' + name + ' <' + email + '>, ' + ', '.join(years) + '.'
    credits = credits.replace(line, new_line)
else:
    new_line = '# ' + name + ' <' + email + '>, ' + year + '.\n'
    credits += new_line

with open(sys.argv[3], 'w') as f:
    f.write(credits + crowdin_contents)
