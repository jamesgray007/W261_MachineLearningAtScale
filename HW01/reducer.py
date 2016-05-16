#!/usr/bin/python

#HW 1.5 - Reducer Function
from __future__ import division
import sys
from math import log
emails={}
words={}
spam_email_count=0 #number of emails marked as spam
spam_word_count=0 #number of total (not unique) words in spam emails
ham_word_count=0 #number of total (not unique) words in ham emails

for chunk in sys.argv[1:]:
    with open (chunk, "r") as myfile:
        for i in myfile.readlines():
            
            #parse the line
            result=i.split("\t")
            email=result[0]
            spam=int(result[1])
            word=result[2]
            
            #initialize storage for word/email data
            if word not in words.keys():
                words[word]={'ham_count':0,'spam_count':0}
            if email not in emails.keys():
                emails[email]={'spam':spam,'word_count':0,'words':[]}
                if spam==1:
                    spam_email_count+=1
                
            #store word data 
            if spam==1:
                words[word]['spam_count']+=1
                spam_word_count+=1
            else:
                words[word]['ham_count']+=1
                ham_word_count+=1
                
            #store email data 
            emails[email]['words'].append(word)
            emails[email]['word_count']+=1

#Calculate stats for entire corpus
prior_spam=spam_email_count/len(emails)
prior_ham=1-prior_spam
vocab_count=len(words)#number of unique words in the total vocabulary
            
for k,word in words.iteritems():
    #These versions calculate conditional probabilities WITH Laplace smoothing.  
    #word['p_spam']=(word['spam_count']+1)/(spam_word_count+vocab_count)
    #word['p_ham']=(word['ham_count']+1)/(ham_word_count+vocab_count)
    
    #Compute conditional probabilities WITHOUT Laplace smoothing
    word['p_spam']=(word['spam_count'])/(spam_word_count)
    word['p_ham']=(word['ham_count'])/(ham_word_count)

#At this point the model is now trained, and we can use it to make our dpredictions
for j,email in emails.iteritems():
    
    #Log Version - not used
    p_spam=log(prior_spam)
    p_ham=log(prior_ham)
    
    p_spam=prior_spam
    p_ham=prior_ham
    for word in email['words']:
        try:
            #p_spam+=log(words[word]['p_spam']) #Log Version - not used
            p_spam*=(words[word]['p_spam'])
        except ValueError:
            continue #This means that words that do not appear in a class will use the class prior
        try:
            #p_ham+=log(words[word]['p_ham']) #Log Version - not used
            p_ham*=(words[word]['p_ham'])
        except ValueError:
            continue         
    if p_spam>p_ham:
        spam_pred=1
    else:
        spam_pred=0
        
    #print spam_pred, email['spam'],p_spam,p_ham,j
    print j+'\t'+str(email['spam'])+'\t'+str(spam_pred)