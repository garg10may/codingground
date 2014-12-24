

def char_freq(x):
    d={}
    for i in x:
        d[i] = d.get(i,0)+ 1
    print d
    

char_freq("abbabcbdbabdbdbabababcbcbab")