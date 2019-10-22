#!/usr/bin/python3

# author: github.com/a37h
# 2019

kInputFileName = 'README.md'
kNameLinkSeparator = '	'  # current symbol is a tab which will cause output to be split into 2 colums in Excel
kLinesSeparator = '\n'  # current symbol is a newline which will cause output to be split into rows in Excel
kOutputFile = 'README_processed.txt' 
# OUTPUT_FILE = None  # uncomment this not to save any output to file


readme = [x.strip() for x in open(kInputFileName, 'r')]
if kOutputFile:
    out = open(kOutputFile, 'w')


# remove the unnecessary stuff
for i in range(len(readme)):
    if '|---|---|---|---|' in readme[0]:
        break
    else:
        del readme[0]
del readme[0]


# process each line and gather company name and applying link
for row in readme:
    r = [x.strip() for x in row.split('|')][1:-1]
    company = r[0].split('](')
    name, link = company[0][1:], company[1][:-1]
    print(name, link, sep=kNameLinkSeparator, end=kLinesSeparator)

    if kOutputFile:
        out.write(name + kNameLinkSeparator + link + kLinesSeparator)
