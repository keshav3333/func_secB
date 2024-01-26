'''
filter(function, iterable)
Construct an iterator from those elements of iterable for 
which function returns true.

a=[1,0,True,'','str',[1,2,3],78,0.0]
output=[1,True,'str',[1,2,3],78 ]

map(function, iterable, ...)
Return an iterator that applies function to every item of iterable, 
yielding the results


'''
def fun(arg):
    if type(arg) in [str,tuple,list,set,dict]:
        return len(arg)
    else:
        return arg
a=[1,2,[4,5,6],'xyz',(4,1,2,3)]
print(list(map(fun,a)))




