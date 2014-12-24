

import re

def correct(x):
    x=x.replace('.','. ')
    x=re.sub(' +',' ',x)
    print x
    
    
correct("This   is  very funny  and    cool.Indeed!") 