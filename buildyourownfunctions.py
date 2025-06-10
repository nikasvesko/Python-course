#using def
def print_lyrics():
  print("Im a lumberjack and IM okay")
  print("I sleep all night and work all day")

#invoking
print_lyrics()
#output are two lines of code, line 3 and 4

big=max("hello world")  

def greet(lang): #lang is parameter
  if lang== "es":
    print("hola")
  elif lanf == "fr":
    print("bonjour")
  else:
    print("hello")
greet("en")
#output is hello

#return values

def greet():
  return "hello"
print(greet(), "glenn")
print(greet(), "sally")

#output is hello glenn or hello sally
#fruitful function returns something, it has a result

print(greet("fr"), "Michael")
#output is bonjour Michael

#you can have more paramteres and arguments
#void functions that do not return a value

#organize your code, do not repeat yourself, if something is long break it into logical chunks and put those chunks in functions and you can make a library of stuff that you use over and over







