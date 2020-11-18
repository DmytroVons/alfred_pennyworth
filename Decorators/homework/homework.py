import logging


# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    def adder(*args):
        return func(*args) * 2

    return adder



def plus_1(a, b):
    return a + b


@double_result
def plus_2(a, b):
    return a + b


# 2. only_even_parameters
# This decorator function should only allow a function to have even parameters,
# otherwise return the string "Please only use even numbers!"

def only_even_parameters(func):
    # if args passed to func are not even - return "Please only use even numbers!"
    def even_number(*args):
        for arg in args:
            if arg % 2 != 0:
                raise TypeError("Please only use even numbers")
            else:
                return args
        return func

    return even_number


@only_even_parameters
def add(a, b):
    return a + b


@only_even_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


# 3. logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)

    # log function arguments and its return value
    def printer(*args, **kwargs):
        logging.info(f'args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Result: {result}')
        print(f'kwargs: {kwargs}, args: {args}, \nresult is: {result}')
        return result

    return printer


@logged
def func(*args):
    return 3 + len(args)


# you called func(4, 4, 4)
# it returned 6


# 4. type_check (see pass_args_to_decorator.py from lecture for example)
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print("Bad Type"), otherwise function should be executed.

def type_check(correct_type):
    def checker(func):
        def pass_function(arg):
            if type(arg) == correct_type:
                return func
            else:
                print("Bad Type")
                pass

        return pass_function

    return checker


@type_check(int)
def times2(num):
    return num * 2


@type_check(str)
def first_letter(word):
    return word[0]


if __name__ == 'main':
    #   task 1
    plus_1(5, 5)  # 10
    plus_2(5, 5)  # 20
    #   task 2
    a1 = add(5, 5)  # "Please add even numbers!"
    b2 = add(4, 4)  # 8
    print(b2)
    print(a1)
    #   task 3
    func(4, 4, 4)
    #   task 4
    print(times2(2))
    times2('Not A Number')  # "Bad Type" should be printed, since non-int passed to decorated function
    print(first_letter('Hello World'))
    first_letter(['Not', 'A', 'String'])  # "Bad Type" should be printed, since non-str passed to decorated function
