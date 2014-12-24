

import string

def char_freq_table(x):
    f = open(x)
    d={}
    for i in f.read():
        d[i] = d.get(i,0) +1
    print d    
    
    new=[ i for i in d.keys() if i in string.letters[:52]]
    
    for i in sorted(new):
        print "%s : %s " % (i,d[i])
    
        

char_freq_table('34.txt')