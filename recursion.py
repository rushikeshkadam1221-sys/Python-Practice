def show(n):
    if (n == 0):
        return 
    print(n)
    show(n-1)

show(3) 

def fact (n):
    if (n == 0 or n == 1):
        return 1
    else: 
        return n * fact(n-1)

print(fact(5)) 

#sum of first n natural numbers 
def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n 
sum = calc_sum(5)
print(sum) 

#print all elements in list. 
def print_list(list, idx):
    if (idx == len(list)):
        return
    print(list[idx]) 
    print_list(list, idx + 1) 

fruits = ["apple", "banana", "cherry", "date"]

print_list(fruits, 0)