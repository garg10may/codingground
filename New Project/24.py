


def make_3sg_form(x):
    if x.endswith('y'):
        x= x[:-1] + 'ies'
    elif x.endswith(('o','s','x','z','sh','ch')):   #passing a tuple of values
        x += 'es'
    else:
        x += 's'
    print x

make_3sg_form('fix')