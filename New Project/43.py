'''
def anagram():
    f=open('unixdict.txt')
    f_copy=open('unixdict2.txt')
    f2=open('result_anagram.txt','w')
    for word in f.read(10).split('\n'):
        print word
    	count =0
    	f_copy.seek(0)
    	for word2 in f_copy.read().split('\n'):
    		if sorted(word)==sorted(word2):
    			count += 1
    			if count >=2:
    				f2.write( word + ", " + word2 + " are anagrams" + '\n' )


anagram()

# this would work but 20K seconds, since takes approx. 1 sec to 
# iterate for each word against 20k words

'''




import urllib

def anagram():
    f=urllib.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt')
    words = f.read().split('\n')
    d={''.join(sorted(x)):[]  for x in words}
    for x in words:
    d[''.join(sorted(x))].append(x)
    max_len= max( len(v) for k,v in d.iteritems())
    for k,v in d.iteritems():
    	if len(v)>=max_len:
    		print v
  
anagram()