import re
data='''
vndkfnklsjvlksdcn,dcgjap01h736873ap 32 k 4857498euieap16k 98976'
'''
pattern='[Aa][Pp] ?[0-3][1-9] ?[A-Za-z] ?[0-9]{4}'
data=re.findall(pattern,data)
print(data)