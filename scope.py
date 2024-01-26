def func(a,b,out=0):
    if len(a)==len(b):
        for i,j in zip(a,b):
            if i!=j:
                out+=1

        return out
    return 'string length not same'
      
print(func('lip','pilh'))
'''
lambda An anonymous inline function consisting of a
single expression
which is evaluated when the function is called. 
The syntax to create a lambda function is 
lambda [parameters]: expression
'''