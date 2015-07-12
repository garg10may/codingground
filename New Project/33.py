



'''def semordnilap(x):
    print "==========================================="
    f = open(x)
    words =  f.read().split('\n')
    for k in words:
        for j in words:
            if k[::-1]==j:
                print k + " " + j + " are palindrome pairs"


semordnilap('33.txt')'''

'''
def is_semordnilap(filepath):
    file = open(filepath)
    words = file.read().split()
    results = []
    for word1 in words:
        for word2 in words:     # using two loops here will cause error since it will also print words which are palindromes
            if word1 == word2[::-1]:
                results.append(word1)
    return results
    
    
print is_semordnilap('34.txt')
'''

def semordnilap(x):
    f = open(x).read()
    words = f.split('\n') 
    while words:
        a = words[0]
        words.remove(a)
        if a[::-1] in words:
            print a + ' and ' + a[::-1] + ' are semordnilap'
                
semordnilap('33.txt')
