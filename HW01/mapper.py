#!/usr/bin/python

#HW 1.5 - Mapper Function
import sys
import re
WORD_RE = re.compile(r"[\w']+")
filename = sys.argv[1]
with open (filename, "r") as myfile:
    for num,line in enumerate(myfile.readlines()):
        fields=line.split('\t') #parse line into separate fields
        # parse the subject and body fields from the line, and combine into one string
        subject_and_body=" ".join(fields[-2:]).strip()
        words=re.findall(WORD_RE,subject_and_body)
        for word in words:
            # ID \t SPAM_flag \t word 
            print fields[0]+'\t'+fields[1]+'\t'+word+'\t1'