#numeric expressions
xx=2
xx=xx+2
print(xx)

jj=23
kk=jj%5  #% is remainder
print(kk)

#operator precedence
#parenthesis, power, multiplication, addition and left to right
#power je potencija, **
#cannot add 1 to a string (ee+1)

type(eee)
type(1)
#intagers->cijeli brojevi
#floating point numbers-> decimalni

print(float(99)) #there is also int

#intager division
print(10/2)
#you get a floating point result

#string conversions
sval= "123"
type(sval)
print(sval+1)
#doesnt work
ival=int(sval)
type(ival)
print(ival+1)

#user input, stane da ti mozes natipkat
nam=input("Who are you?")
print("Welcome", nam)
#i onda se postavi pitanje i dobijes odg welcome to sto si napisao

inp=input("Europe floor?")
ufos= int(inp)+1 #input gives you a string so you have to use int here
print("US floor", ufos)
