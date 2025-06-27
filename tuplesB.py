#sorting lists of tuples
d={'a':10,'b':1,'c':22}
d.items()
#stavi sve u parove, ali a c b

sorted(d.items())
#bit ce a b c

for k, v in sorted(d.items()):
  print(k,v)
#printa sortano

c={'a':10,'b':1,'c':22}
tmp=list()
for k,v in c.items():
  tmp.append( (v,k) ) #temporarily
print(tmp)
#doci ce prvo value pa key 
tmp=sorted(tmp,reverse=True)
print(tmp)
#sve ce bit obrnuto, najveca vrijednost prvo jer je reverse

fhand=open('romeo.txt')
counts=dict()
for line in fhand:
  words=line.split()
  for word in words:
    counts[word]=counts.get(word,0)+1

lst=list()
for key, val in counts.items():
  newtup=(val,key)
  lst.append(newtup) #making a new tuple
lst=sorted.(lst,reverse=True)
for val, key in lst[:10]:  #top ten most common words
  print(key,val)  

