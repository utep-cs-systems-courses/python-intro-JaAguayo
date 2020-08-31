#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re 
import sys
import subprocess # executing program
import os         # checking if file exists

if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()


inputFname = sys.argv[1]
outputFname = sys.argv[2]

#first check to make sure program exists
if not os.path.exists("wordCount.py"):
    print ("wordCount.py doesn't exist! Exiting")
    exit()

#make sure text files exist
if not os.path.exists(inputFname):
    print ("text file input %s doesn't exist! Exiting" % inputFname)
    exit()

#execute the program with 
subprocess.call(["python3", "./wordCount.py", inputFname, outputFname])

word_count = {}
    
with open('speech.txt', 'r') as inputFile:
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

sortWords =  dict(sorted(word_count.items(),key=lambda item: item[0]))
        