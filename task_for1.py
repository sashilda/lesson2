import random 
mylist = list(range(10))
random.shuffle(mylist)

for n in mylist:
    print("n: {}\tn+1: {}".format(n,n+1))