


def palindrome(x):
    striped=[]
    for i in x:
        if i.isalpha():
            striped.append(i.lower())
    if striped==striped[::-1]:
        print "Palindrome"
    else:
        print "not a palindrome"
        
        
        
palindrome("Dammit, I'm mad!")