import random


class Scale:

    def __init__(self, scale_key):
        self.scale_key = scale_key


class Guitare:

    def __init__(self, tempo, scale):
        self.tempo = tempo
        self.scale = scale

    def play_score(self):
        print(f'John Lennon play {self.scale.scale_key} scale in {self.tempo} beats per minute.')


if __name__ == '__main__':
    scale = Scale(f"{random.choice(['c', 'd', 'e', 'f', 'g', 'a', 'h'])} {random.choice(['major', 'minor'])}")
    guitare = Guitare(int(random.randint(40, 200)), scale)
    guitare.play_score()
