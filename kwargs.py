# Write a function that takes an unknown number of arguments and returns their sum.

def sum_numbers(a,b):
    sum=0
    result=a+b
    return result
    print(sum_numbers(70,80))
    


#  Write a function that takes two arguments, the first being a string and 
#  the second being an unknown number of integers. The function should return a
#   new string where the integers have been added to the original string.

def add_numbers(string,*numbers):
    numbers_str="".join(str(num)for num in numbers)
    new_string=string+numbers_str
    return new_string
    add_numbers("Hello mercy" " ",3,7,8,9)



#  Write a function that takes an unknown number of keyword arguments and
#  returns a dictionary where the keys are the argument names and the values are the argument values.
def create_dictionary(** nums):
    return nums
    create_dictionary(name="mercy",age=50,gender="female",weight=20.8)




#  Write a function that takes a function and an unknown number of arguments, 
# and returns the result of calling the function with the arguments.



#  Write a function that takes a list of integers and an unknown number of keyword arguments.
#  The function should return a new list where each integer in the original list has been multiplied
#   by the value of the corresponding keyword argument.


# def multiply_kwargs(**kwargs):
#     result=[]
#     for num in kwargs:
        
#         num*=kwargs
#         result.append(num)
        
#     return result

# kwargs=[56,70,60]
# result =multiply_kwargs(kwargs)
# print(result)


# Write a function that takes a list of integers and an unknown number of additional integers 
# as arguments. The function should return the index of the first occurrence of the sum of the 
# # list and the additional integers


#  Write a function that takes an unknown number of keyword arguments, each with a string value.
#    The function should concatenate all the strings and return the resulting string.


def concatenate_strings(kwargs):
    return " ".join(kwargs.values())
    result=concatenate_strings(a="hello",b="world")
    print(result)

