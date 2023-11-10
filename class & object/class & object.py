class animal:
    name = "" # properties/atribute
    color = ""

    def makesound(self, sound):
        print("animal is making sound")
    
    def eat(self, food):
        print("animal is eating", food)

    def sleep(self):
        print("animal is sleeping")

cat = animal()
cat.name = "Morinaga"
cat.color = "black"
cat.sleep()
cat.eat("fish")