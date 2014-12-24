



'''def semordnilap(x):
    print "==========================================="
    f = open(x)
    words =  f.read().split('\n')
    for k in words:
        for j in words:
            if k[::-1]==j:
                print k + " " + j + " are palindrome pairs"


semordnilap('33.txt')'''

def is_semordnilap(filepath):
    file = open(filepath)
    words = file.read().split()
    results = []
    for word1 in words:
        for word2 in words:
            if word1 == word2[::-1]:
                results.append(word1)
    return results
    
    
print is_semordnilap('34.txt')