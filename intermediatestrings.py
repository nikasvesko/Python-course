s="monty python"
print(s[0:4])
#up to but not including

#if you put a bigger number its not going to traceback you
#it will just put everything till the end
print(s[:])
#prints everything

#using in
fruit="banana"
"n" in fruit
#true
"m" in fruit
#false

#string comparison
if word == "banana" :
  print("all right, bananas")
if word< "banana":
  print("your word" + word +", comes before banana.")
elif word>"banana":
  print("your word" + word + ", comes after banana.")
else:
  print("all right, bananas.")

#string library, string objects has built in capabilities
greet= "hello Bob"
zap=greet.lower()
print(zap)
#daje hello bob, lowercase, lower je string

stuff="hello world"
type(stuff)
dir(stuff)
#napisu se methods

#searching a string
fruit="banana"
pos=fruit.find("na")
print(pos)
#types 2

