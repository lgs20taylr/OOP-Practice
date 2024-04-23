# Zoo Animals
class animal:
    def __init__(self, height, length, weight, sex):
        self.height = height
        self.length = length
        self.weight = weight
        self.sex = sex

    def getTaller(self, amount):
        self.height += amount

    def elongate(self, amount):
        self.length += amount


# * Mammals
class mammal(animal):
    def __init__(self, height, length, weight, sex, furColour):
        super().__init__(height, length, weight, sex)
        self.hotBlood = True
        self.furColour = furColour


# * Birds
class bird(animal):
    def __init__(self, height, length, weight, sex, featherColour):
        super().__init__(height, length, weight, sex)
        self.hotBlood = False
        self.laysEggs = True
        self.featherColour = featherColour


# * Reptiles
class reptile(animal):
    def __init__(self, height, length, weight, sex, scaleColour):
        super().__init__(height, length, weight, sex)
        self.hotBlood = False
        self.laysEggs = True
        self.scaleColour = scaleColour
