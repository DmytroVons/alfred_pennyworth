'''
Task 1. Під мостом завівся Троль, який систематично і бездушно забирає плату за прохід мостом
Оскільки ми проти расизму, то допоможемо Тролю правильно забирати кошти в людей.
Створіть декоратор Troll, та застосуйте його до функції bridge, по якій ходять люди Person.
За прохід по мосту в них віднімаються кошти, якщо їх достатньо.
Якщо ні, то TrollIsAngry exception не дасть людині перейти міст!
'''
TROLL_TAX = 50


class TrollIsAngry(Exception):
    pass


class Person:

    def __init__(self, money):
        self.money = money


def troll(function):
    def wrapper(*args, **kwargs):
        person = args[0]
        if person.money >= TROLL_TAX:
            person.money -= TROLL_TAX
        else:
            raise TrollIsAngry
        return function(*args, **kwargs)

    return wrapper


@troll
def bridge(person: Person):
    print(f"Person passed the bridge with money {person.money}")
    return


'''
Task 2. Створіть декоратор (Timer), який засікає час роботу функції. Для створення декоратора використайте class, а не function.

adding a decorator to the function 
@Timer
def some_function(delay): 
    from time import sleep 

    # Introducing some time delay to  
    # simulate a time taking function. 
    sleep(delay) 

some_function(3)
'''
import time


class Timer:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time() - t1
            print(f'{func.__name__} ran in: {t2} sec')
            print(f"{self.name} finished work")
            return result

        return wrapper


@Timer('timer_class')
def my_func():
    time.sleep(1)


'''
Task 3. recursion + factorial
Нашіть функцію, яка рекурсивно рахує факторіал, а заодно декоратор, який перевіряє чи вхідне значення ціле та позитивне число:

def argument_test_natural_number(f):
    # check is arg to f is int and > 0, raise error otherwise
'''


def decorator(func):
    def wrapper(num):
        if num > 0 and type(num) == int:
            return func(num)
        else:
            raise ValueError('You shoud input positive number and int')

    return wrapper


@decorator
def factorial(n):
    return factorial(n - 1) * n if n != 1 else n


'''
Task 4. Напишіть программу, яка виводить частину послідовності 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 .... 
 На вхід приймається значення n - кількість елементів послідовності, які мають бути виведенні 

Наприклад, якщо n = 7, то программа має вивести 1 2 2 3 3 3 4.
Sample Input:
7
Sample Output:
1 2 2 3 3 3 44. Напишіть программу, яка виводить частину послідовності 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 .... 
 На вхід приймається значення n - кількість елементів послідовності, які мають бути виведенні 

Наприклад, якщо n = 7, то программа має вивести 1 2 2 3 3 3 4.
Sample Input:
7
Sample Output:
1 2 2 3 3 3 4
'''


def count(func):
    def wrapper(n):
        for i in range(n):
            print(str(i) * i, end='\n')
        return func

    return wrapper


@count
def number(number1):
    return number1


'''
Task 5. Напишіть програму, яка зчитує з консолі числа (по одному в строці) до тих пір,
пока сума сум введених чисел не буде рівною 0 і, відповідно, після цього виводить сумму квадратів усіх введених чисел.
У прикладі ми зчитуємо числа 1, -3, 5, -6, -10, 13; в цей момент помічаємо, що сума цих чисел рівна 0.
і виводим сумму їх квадратів зупиняючи зчитування з консолі.
Sample Input:
1
-3
5
-6
-10
13
4
-8
Sample Output:
340
'''


def get_number():
    l = []
    is_zero_sum = True
    while is_zero_sum:
        a = int(input('Please input one number(- or +), while sum of your list numbers will be 0: '))
        l.append(a)
        if sum(l) != 0:
            print(l)
            print(f'This is sum of your numbers: {sum(l)}')
            continue
        else:
            print('The sum of your numbers is Zero!')
            m = [i * i for i in l]
            print(f'The quater of your numbers is: {sum(m)}')
            is_zero_sum = False


'''
Task 6. Одне із застосувань множинного успадкування - розширення функціональності класу якимось заздалегідь 
визначеним способом.
Наприклад, якщо нам знадобиться залогувати якусь інформацію при зверненні до методів класу.
Розглянемо класс Loggable:
```
import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
```

У нього є рівно один метод log, який дозволяє виводити в лог (в даному випадку в stdout) якесь повідомлення,
додаючи при цьому поточний час.
Реалізуйте клас LoggableList, унаслідував його від класів list і Loggable таким чином,
щоб при додаванні елемента в список за допомогою методу append в лог відправлялося повідомлення,
що складається з тількищо доданого елемента.
'''
import time


class Loggable:

    def log(self, msg):
        print('{}: {}'.format(time.ctime(), msg))
        return


class LoggableList(Loggable, list):

    def __init__(self, data):
        super().__init__(data)

    def append(self, element):
        super().append(element)
        self.log(msg=element)


'''
7. Реалізуйте клас PositiveList, унаслідував його від класу list, для зберігання позитивних цілих чисел.
Також реалізуйте нове виключення NonPositiveError.
У класі PositiveList перевизначите метод append (self, x) таким чином, щоб при спробі додати
 непозитивним ціле число викликалося виключення  NonPositiveError і число не додавалося,
 а при спробі додати позитивне ціле число, число додавалося б як в стандартний list.
'''


class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, num):
        if num > 0 and type(num) == int:
            super().append(num)
        else:
            raise NonPositiveError("Your number isn`t positive")


if __name__ == 'main':
    pass
# task 1
#    vasya = Person(300)
#    bridge(vasya)
# task 2
#    my_func()
# task 3
#    print(factorial(5)))
# task 4
#    number1 = int(input('Set your number: '))
#    number(number1)
# task 5
#    get_number()
# task 6
#    log_list = LoggableList([1, 2, 3])
#    log_list.append(4)
#    print(log_list)
# task 7
#    num = PositiveList([])
#    num.append(-1)
#    print(num)
