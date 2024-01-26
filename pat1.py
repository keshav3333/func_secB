rows = int(input('enter number of rows :- '))
temp= rows//2
out=''
for i in range(rows):
    for j in range(rows):
        if i==temp or j==temp:
            out+='  '
        else:
            out+='* '
    out+='\n'

print(out)
# name = input('enter file name :- ')
# with open(f'{name}.txt','w') as file:
#     file.write(out)