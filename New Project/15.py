

def find_longest_word(x):
    k=[]
    for i in x:
        k.append(len(i))
    print max(k)
    

find_longest_word(['the','tanmay','how are you'])