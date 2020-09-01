#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re 
import sys

inputFname = sys.argv[1]
outputFname = sys.argv[2]

word_count = {}

with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        # split line on whitespace and punctuation
        words = re.split('\W+', line)
        for word in words:
            if word.lower() in word_count:
                word_count[word.lower()] += 1
            else:
                word_count[word.lower()] = 1
                
sort_words =  dict(sorted(word_count.items(),key=lambda item: item[0]))
del sort_words['']

with open(outputFname, 'w') as outputFile:
    for k,v in sort_words.items():
        print(k,v, file=outputFile)

 