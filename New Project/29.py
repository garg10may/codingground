


def filter_long_words(x,n):
    return filter(lambda x: len(x)>n,x)
    
    
print filter_long_words(['tanmay','a','how'],2)