#tuples are like lists, another kind of sequence
x=('Glenn','Sally','Joseph')
print(x[2])
y=(1,7,9)
print(y)
print(max(y))
#it will print 9
for iter in y:
  print(iter)
#isprintat ce svaki broj u svojem lajnu
#tuples are immutable, like strings
#you will get a traceback
# you cannot sort them, append them or reverse them
#like not mutable list
t=tuple()
dir(t)
#count and index, we like them bc they are more efficient
#temporary variables, better memory use
(x,y)=(4,'fred')
print(y)
d=dict()
d['csev']=2
d['cwen']=4
for (k,v) in d.items():
  print(k,v)
#printat ce csev 2 cwen 4
#k is key, v is value
#items method returns list of tuples
#they are comparable
#samo gleda prvi broj, ako ne moze odg onda gleda drugi par
#u Sally i Sam, l je manje od m pa ce Sally bit manje-> string comparison

  
