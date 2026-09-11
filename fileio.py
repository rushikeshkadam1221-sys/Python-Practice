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
import os 
os.remove("recursion.py") 


with open("practice.txt","w") as f:
    f.write("Hi everyone\n we are learning file I/O \n using Java \n I like programming in Java")