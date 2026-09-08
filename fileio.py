#open, read & close a file before writing or reading a file.
 
f = open("miniproject.py", "r") 
data = f.read(12)
print(data)  
print(type(data))
f.close() 


