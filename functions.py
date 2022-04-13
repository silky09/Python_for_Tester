from unittest import result


print("hello", " world")
other_print = print
other_print("This is another print")

print("--------------------------------------------")
# simple and long way
num1 = 10
num2 = 10
result = num1 + num2
result = result + 10
result = result * 5
result = result / 10
print(result)

# using function

def my_result(sem1, sem2):
    result = sem1 + sem2
    result = result + 10
    result = result * 5
    result = result / 10
    return result
print("Using function: ", my_result(10, 10))

print("-----------------------------------")

#we can define value in arguments
def my_result(sem1, sem2 = 10):
    result = sem1 + sem2
    result = result + 10
    result = result * 5
    result = result / 10
    return result
print("Using function: ", my_result(10))
print("another example: ", my_result(20, 20))

import operator
print("Adding two numbers 20 and 20 is:", operator.add(20, 20))
print("Light is off: ", operator.not_(True))
