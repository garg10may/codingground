

def max(l):
    max=0
    for i in range(len(l)-1):
        if l[i]>l[i+1] and l[i]>max:
            max=l[i]
        elif l[i+1]>max:
            max=l[i+1]
    print max
        
        

max([1,3,6,9,6,4,2,6])