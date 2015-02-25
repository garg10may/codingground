

def count(n):
    k=[]
    for i in n:
        k.append(len(i))
    print k
        
def count1(n):
    print map(lambda x:len(x), n)
 
def count3(n):
    print map(len,n)
    
def count2(n):
    print [len(i) for i in n]

count(['tanmay','how are you','montecarlo'])
count1(['tanmay','how are you','montecarlo'])
count2(['tanmay','how are you','montecarlo'])
count3(['tanmay','how are you','montecarlo'])
