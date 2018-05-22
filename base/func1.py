import functools as fct

int2= fct.partial(int, base=2)

print( int2('100001'))