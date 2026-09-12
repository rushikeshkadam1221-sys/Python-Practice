#open, read & close a file before writing or reading a file.

#read a file 
f = open("miniproject.py", "r") 
data = f.read(12)
print(data)  
print(type(data))
f.close() 

 
#write a file
f = open("recursion.py", "w")
f.write("Hello, Welcome to the world of Recursion")
f.close() 

f = open("recursion.py", "r+")   #overwrite the file
f.write("abc")
f.close() 

#with syntax 
with open("recursion.py", "r") as f:
    data = f.read()
    print(data) 

with open("recursion.py", "w") as f:
    f.write("new data")

#Delete a file 
from ast import With
import os 
os.remove("recursion.py") 


with open("practice.txt","w") as f:       # use with open syntax to write to a file
    f.write("Hi everyone\n we are learning file I/O \n using Java \n I like programming in Java")

word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Word found!")
    else:
        print("Word not found!") 

 #from a file containing numbers separated by commas, print the sum of the count of even numbers. 1,2,45,55,86,76
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)