
def overlapping(m,n):
    for i in m:
        if i in n: 
            status=1
            break
        else:
            status =0
    if status ==1:
        print True
    else:
        print False
        
        
        
overlapping([1,2,3,3,0],[0,6,7,8,9])


