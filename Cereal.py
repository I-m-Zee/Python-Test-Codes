
class Cereal:
    def __init__(self, str1, str2, init1):
        self.name = str1
        self.brand = str2
        self.fiber = init1
    def __str__(self):
        return "{} is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand, self.fiber)

c1 = Cereal("Corn Flakes", "Kellogg's",2)
c2 = Cereal("Honey Nut Cheerios", "General Mills",3)
print(c1)
print(c2)