import random


class MemorySequence:
    # ASCII Numbers = 48 - 57
    # ASCII Letters = 65 - 90
    # ASCII Lowercase = 97 - 122
    _ASCII_RANGES = [(48, 57), (65, 90), (97, 122)]

    def __init__(self):
        self.length = 0
        self.sequence = []
        self.shuffled_sequence = []

    def set_length(self, length: int):
        self.length = length

    def generate_sequence(self):
        self.sequence = [
            chr(random.randint(*random.choice(self._ASCII_RANGES)))
            for _ in range(self.length)
        ]

    def shuffle_sequence(self):
        shuffled_sequence = self.sequence.copy()
        random.shuffle(shuffled_sequence)
        self.shuffled_sequence = shuffled_sequence

    def __repr__(self):
        return "".join(self.sequence)

    def __str__(self):
        return " ".join(self.sequence)
