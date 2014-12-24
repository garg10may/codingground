

def translate(x):
    l=[]
    for i in x:
        if i not in ('aeiou'):
            l.append(i +'o' +i)
        else:
            l.append(i)
    print ''.join(l)
    

translate('this is fun')
            