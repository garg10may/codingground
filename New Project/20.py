



def translate(x):
    new=[]
    d = {
    "merry":"god", 
    "christmas":"jul", 
    "and":"och",
    "happy":"gott",
    "new":"nytt", 
    "year":"ar"
    }
    l=x.split(' ')
    for i in l:
        new.append(d[i])
    print new 

translate("merry new christmas and happy new year")
    