

def filter_long_words(x,n):
    k=[]
    for i in x:
        if len(i)>n:
            k.append(i)
    print k
    

filter_long_words(['the','tanmay','how are you'],6)
            