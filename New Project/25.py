


def make_ing_form(x):
    if x.endswith('e') and not (len(x)<3 or x[-2]=='e' or
    x[-2]=='i'):
        x = x[:-1] + 'ing'
    elif x.endswith('ie'):
        x= x[:-2] + 'ying'
    elif len(x)==3 and x[-2]  in('aeiou') and x[-1] not in ('aeiou'):
        x = x + x[-1] + 'ing'
    else:
        x += 'ing'
    print x
    
make_ing_form('lie')
make_ing_form('see')
make_ing_form('move')
make_ing_form('hug')