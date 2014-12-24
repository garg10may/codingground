



def palindrome(x):
    f = open(x)
    for i in f.read().split('\n'):
        if i[::-1]==i :
            print i + " is palindrome"
    f.close()
    
palindrome('32.txt')