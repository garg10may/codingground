

import string

def pangram(x):
    status=0
    for i in string.letters[:26]:
        if i in x.lower():
            status=1
        else:
            print "not a pangram"
            status=0
            break
    if status ==1:
        print "Pangram"
        
        
        
pangram("The quick brown fox jumps over the lazy dog")