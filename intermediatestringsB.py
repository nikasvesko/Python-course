greet= "hello Bob"
nstr= greet.replace("Bob", "Jane")
print(nstr)
#it will display hello Jane

nstr= greet.replace("o", "X")
print(nstr)
#it will display hellx Bxb

#stripping whitespace
greet="  hello Bob  "
greet.lstrip() #removes whitespace

#lstrip is left, rstrip is right
#prefixes
line="please have a nice day"
line.startswith("please")
#it will display TRUE
line.startswith ("P")
#FALSE

#parsing and extracting
data= "from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos=data.find("@")
print(atpos)
#it will say 21 cause its on that spot
sppos=data.find(" ", atpos)
print(sppos) #razmak nakon monkeya
#extracting
host= data[aptos+1:sppos]
print[host]
#dobivamo dio maila za sk

#two kinds of strings
#Unicode is in Python 3
#it understands international character sets
#good for exchanging data







