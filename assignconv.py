x = input()
if x[-1] in ['j','J']:
    val = eval(x[:-1])/4.186
    print('{:.3f}cal'.format(val))
else:
    val = eval(x[:-3])*4.186
    print('{:.3f}J'.format(val))

