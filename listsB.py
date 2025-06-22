#lists using +

a= [1,2,3]
b=[4,5,6]
c= a + b

print(c)
#dobit cemo novu listu s a i b spojeno

#lists se mogu i rezat koristeći :
t= [9,41,12,3,74,15]
t=[1:3]
#dobit cemo 41 i 12, a broj koji je pod pozicijom 3 nećemo jer ide samo do trece pozicije, ne ukljucuje ju
t[:]
#dobit cemo sve

#list methods

x= list()
type(x)

#doci ce type list
dir(x)
#izlistat ce metode

#building a list from scratch
stuff=list() #empty list unutar stuffa
stuff.append("book")
stuff.append(99)
print(stuff)
#doci ce book i 99 u uglatim

stuff.append("cookie")
print(stuff)
#dodan je cookie

#in operator 
#kao sa strings, dobit ćeš true and false logicke operatore


#lists are in order

friends=["Joseph","Glenn", "Sally"]
friends.sort()
print(friends)
#bit ce po abecedi

#again, lists are mutable

#built in functions and lists

nums=[3,33,4,5]
print(len(nums))

#we have sum, min, max, average samo podijeli sum s len itd.

total=0
count=0
while True:
  inp= input("Enter a number:")
  if inp=="done" : break
    value= float(inp)
    total = total+value
    count= count+1

average= total/count
print("Average:", average)

#loop for average

#and with a list, uses more memory
numlist= list()
while True :
  inp= input("Enter a number:")
  if inp=="done" : break
  value=float(inp)
  numlist.append(value)

average=sum(numlist) / len(numlist)
print("Average:", average)









