

n= raw_input('Enter the value of N')
count_left, count_right = 0,0
s = [random.choice['[',']'] for i in range(2*n)]
for l,i in enumerate(s):
    if count_left ==count_right and l==ln(s)-1:
        print "balanced"
        print s
        break
    elif i=='[':
        count_left += 1
    elif i==']':
        count_right+=1
    else:
        print "Not balanced"
        print s
        break