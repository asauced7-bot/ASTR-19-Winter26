class Dog:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("This animal is a dog.")
        print(f"Arm length: {self.arm_length}")
        print(f"Leg length: {self.leg_length}")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail: {self.has_tail}")
        print(f"Is furry: {self.is_furry}")
my_dog = Dog(0.5, 1.2, 2, True, True)

my_dog.describe()