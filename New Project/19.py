




def song():
    print "99 bottles of beer on the wall, 99 bottles of beer"
    for i in range(1,98)[::-1]:
        print "take one down, pass it around, " + str(i) + " bottles of beer on the wall"
        
song()