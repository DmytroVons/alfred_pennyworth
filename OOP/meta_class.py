class Basic(type):

    def __new__(metacls, name, bases, attrs):
        cls = type.__new__(metacls, name, bases, attrs)
        """cls is an instance of "Basic"""""
        return cls

if __name__ == '__main__':
    class Foo:
        __metaclass__ = Basic


    class Bar(Foo):
        pass


    print(Foo.__metaclass__)
    print(Bar.__metaclass__)
