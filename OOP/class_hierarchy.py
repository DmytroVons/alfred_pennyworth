class Animal:
    """
    Create new parent-class (base classes)
    """

    def __init__(self, color='black', sex='male'):
        self.color = color
        self.sex = sex

    def __str__(self):
        if self.sex.lower() == 'male':
            sex = 'boy'
        else:
            sex = 'girl'
        print(f'I am a {self.__class__.__name__}. My color is {self.color} and i\'m a {sex}.')

    def walk(self):
        print(self.__class__.__name__, 'can walk')


class Wolf(Animal):
    """
    Create child-class of parent classes Animal (subclasses)
    """

    def say_wolf(self):
        print('I can say aauuufff')


class Tiger(Animal):
    """
    Create child-class of parent classes Animal (subclasses)
    """

    def say_tiger(self):
        print('I can say arrrr')


class Monkey(Animal):
    """
    Create child-class of parent classes Animal (subclasses)
    """

    def say_monkey(self):
        print('I can say y-y-a-a')


class Dog(Animal):
    """
    Create child-class of parent classes Animal (subclasses)
    """

    def say_dog(self):
        print('I can say gav-gav')


class Cat(Animal):
    """
    Create child-class of parent classes Animal (subclasses)
    """

    def say_cat(self):
        print('I can say myau')


if __name__ == '__main__':
    animal = Tiger('white', 'female')
    animal.walk()
    animal.__str__()
