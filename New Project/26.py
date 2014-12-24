



def max_in_list(n):
    return reduce(lambda x,y: max(x,y), n)
    
print max_in_list([1,2,3,8,2,3,4,0,12])