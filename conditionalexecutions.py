#if statement
x=5
if x<10:
    print("smaller")
if x>20:
    print("bigger")

#true and false questions, Boolean questions
# == is equal to
# = is assignment statement

x=5
if x == 5 :
    print("equals 5")
print("afterwards 5") #de-indent, how far does the indention lasts

if x==6 :
    print("is 6")
    print("is still 6")
    print("third 6")
print("afterwards 6")

#indentation goes after : (after for or if statement)
#do not use tabs

#nested decisions
x=42
if x > 1 :
    print("more than one")
    if x <100 :
        print("less than 100")
print("all done") #enda two blocks jer je dva puta de-indentan
#if yes u biti printa ove indentet, ako je ne printa ovaj koji nije indentet

#two-way decisions
x=4

if x> 2:
    print("bigger")
else :
    print("smaller")
print("all done") 