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

f = open("recursion.py", "r+")
f.write("abc")
f.close() 

