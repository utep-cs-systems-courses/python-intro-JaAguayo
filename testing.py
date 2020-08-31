#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:01:26 2020

@author: jaredaguayo
"""
import re

if __name__ == "__main__":
    word_count = {}
    lower_case_words = []
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
    sort_words =  dict(sorted(word_count.items(),key=lambda item: item[0]))
    del sort_words['']
    print(sort_words)
        
    with open("output.txt", 'w') as f:
        for k,v in sort_words.items():
            print(k,v,file=f)
            
    
