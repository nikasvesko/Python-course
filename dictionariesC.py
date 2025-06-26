#counting words in text
#counting pattern
counts=dict()
print('Enter a line of text:')
line=input('')

words=line.split() #split line into words
print('Words:', words)

print('Counting...')
for words in words:
  counts[word]=counts.get(word,0)+1
print('Counts', counts)

#if we run it, prvo upises tekst nakon ovog prvog runa i onda dobijes histogram
#dictionary u stvari

#definite loops and dictionaries
counts={'chuck' :1, 'fred':42, 'jan':100}
for key in counts:
  print(key, counts[key])

#tri puta runna loop, samo dobivamo ime i broj bez dvotocke i icega

jjj={'chuck' :1, 'fred':42, 'jan':100}
print(list(jjj))
#izaci ce samo imena kao lista
print(jjj.keys())
#isto
print(jjj.values())
#samo brojevi
print(jjj.items())
#sve, tuple?

#mozemo dodati iterations variables
jjj={'chuck' :1, 'fred':42, 'jan':100}
for aaa,bbb in jjj.items():
  print(aaa,bbb)
#key-value pairs

name=input('Enter file:')
handle=open(name)
counts=dict()
for line in handle:
  words=line.split()
  for word in words:
    counts[word]= counts.get(word,0)+1

bigcount=None
bigword=None
for word,count in counts.items():
  if bigcount is None or count> bigcount: 
    bigword=word
    big count=count

#kao max loop

print(bigword, bigcount)





