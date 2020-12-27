import random


class Laptop:

    def __init__(self):
        model = Screen(random.choice(['samsung', 'LG', 'apple']))
        resolution = Screen(f'{random.randint(400, 2000)} x {random.randint(600, 1300)}')
        matrix_type = Screen(random.choice(
            ['amoled', 'Twisted Nematic', 'IPS Panel Technology', 'VA Panel', 'Advanced Fringe Field Switching']))
        size = Screen(random.choice(['big', 'medium', 'small']))
        self.result = model, resolution, matrix_type, size

    def __str__(self):
        for res in self.result:
            print(res.parameters)


class Screen:

    def __init__(self, parameters):
        self.parameters = parameters


if __name__ == '__main__':
    laptop = Laptop()
    laptop.__str__()
