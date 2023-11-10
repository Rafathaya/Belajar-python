class animal:
  name = ""
  color = ""

  def __init__(self, name, color):

  def makesound(self, sound): # method
      print(f"{self.name} is {sound}")

  def eat(self, food):
      print(f"{self.name} is eating {food}")

  def sleep(self):
      print(f"{self.name} is sleeping")

cat = animal()
cat.name = "Morinaga"
cat.makesound("meowing")
cat.color = "black"
cat.eat("fish")
cat.sleep()
