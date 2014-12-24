


def translate(x):
    d={"merry":"god", "christmas":"jul",
    "and":"och", "happy":"gott",
    "new":"nytt", "year":"ar"}
    print map(lambda x: d[x], x)
    
translate(['happy','new','year'])
    