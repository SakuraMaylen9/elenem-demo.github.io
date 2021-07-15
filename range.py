# The task of this assignment is to create your own function called my_range(m,n) that returns the same thing as list(range(m,n)), without using the range function. To do this, you can start your function with an empty list [] and use a while loop to count from m to n, adding each number to the list.

def my_range(m, n):
    my_list = []
    while m < n :
        my_list.append(m)
        m += 1
        
    return my_list

print(my_range(0,10))

