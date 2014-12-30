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