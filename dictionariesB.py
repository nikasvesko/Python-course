#most common name
#counters with dictionaries
ccc=dict()
ccc['csev']=1

ccc['csev']=ccc['csev']+1

print(ccc)
#doci ce csev s 2

#tracebacks
#moramo dodati s in u ccc
counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
  if name not in counts:
    counts[name]=1
  else:
    counts[name]=counts[name]+1
print(counts)
#dobit cemo histogram s imenima

if name in counts:
  x=counts[name]
else :
 x=0

x=counts.get(name,0)

#default value if key does not exist
#a ne postoji

counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
  counts[name]=counts.get(name,0)+1
print(counts)
#simplified counting with get

  
  
