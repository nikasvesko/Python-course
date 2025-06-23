#strings and lists
abc= "with three words"
#split looks at spaces
stuff=abc.split()
print(stuff)
#dat ce listu individualnnih riječi

print(len(stuff))
#3
print(stuff[0])
#with has subzero position
print(stuff)
for w in stuff:
  print(w)
#gonna print all three words svaka u svaki red

#ako stavis puno razmaka, racuna ga i dalje kao jedan
#split trazi razmak, ako imamo ; ne radi nego ce stavit sve tri rijeci pod jednu na listi
#ako stavimo split(;) onda radi 

fhand= open("mbox-short.txt")
for line in fhand:
  line= line.rstrip()
  if not line.startswith("From") : continue
  words = line. split()
  print(words[2])
#dobit cemo dan u tjednu

#the double split pattern
#splitamo mail, nazovemo email varijablu i unutra stavimo ono pod 1 i onda mozemo jos jednu varijablu i splitat email po @



