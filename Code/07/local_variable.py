# The 1st level block start
x = 50

def func(x):
    # The 2nd level block start
    print('x is', x)
    x = 2 # this x is local variable in func().
    print('Changed local x to', x)
    # The 2nd level block end

func(x)
print('x is still', x)
# The 1st level block end