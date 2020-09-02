#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re 
import sys

inputFname = sys.argv[1]
outputFname = sys.argv[2]

word_count = {}

#open input file
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        # split line on whitespace and punctuation
        words = re.split('\W+', line)
        for word in words:
            #.lower() makes all words into lowercase, adds to count in the dict if words in dict
            if word.lower() in word_count:
                word_count[word.lower()] += 1
            else:
                word_count[word.lower()] = 1

#sort the words in the dict
sort_words =  dict(sorted(word_count.items(),key=lambda item: item[0]))

#delete the space it was saving in the dict
del sort_words['']

#open output file
with open(outputFname, 'w') as outputFile:
    for k,v in sort_words.items():
        #gets the word and number associated with it in the dict and prints it to the ouput file
        print(k,v, file=outputFile)

 