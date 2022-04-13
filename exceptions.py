# print(1 + 'hi') # it throws an exceptions
# print('Hello there!') 

#so use try and except keywords

def numbers(num1, num2):
    try:
        print(num1 + num2)
        print(num1 - num2)
        print(num1 * num2)
    except Exception:
        print('These value can not be added/substract or multiply, try numbers only!')
        
numbers(1, 'hi')
numbers(2, 5)

#-----------------------------------------------------------
# raise keyword with conditional statements helps
# to identify which line of the code throws exceptions
def my_num(num1, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('inputs must be integer!')
    print(num1 + num2)
    
my_num(2, 7)
my_num(1, 'hi')

# try:
#    my_num('hello', 5)
# except Exception as e:
#     print(f'something went wrong: {e}')
    

    