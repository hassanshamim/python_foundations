"""
Files can have Docstrings at the top
"""

SOME_CONSTANT = 'HOORAY'

# We put our useful functions, variables, and code in general towards the top.
def add(a, b):
    """ Functions can have docstrings too"""
    return a + b



# To run this python file as a script, we use the following conditional
if __name__ == '__main__':
    # This is where the script logic happens
    number1 = int(input('choose a number: '))
    number2 = int(input('choose a number: '))
    result = add(number1, number2)
    print('Those numbers added together are:', result)
