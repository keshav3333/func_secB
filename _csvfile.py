import csv
# file= open('sample.csv',a')
# with open('new.csv','w',newline='') as csvfile:
#     fieldnames=['id','name','age']
#     record=csv.DictWriter(csvfile,fieldnames)
#     record.writeheader()
#     data=[
#         {'id':1,'name':'Rajesh','age':18},
#         {'id':2,'name':'Ramya','age':16},
#         {'id':3,'name':'Balaji','age':2},
#     ]
#     record.writerows(data)

with open('new.csv','r',newline='') as file:
    records=csv.DictReader(file)
    for i in records:
        print(i)

'''A regular expression (or RE) specifies
 a set of strings that matches it'''   