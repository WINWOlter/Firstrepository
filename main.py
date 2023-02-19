class Person:
  height = 170
  age = 13
  name = "Mark"
  is_male = True

  def __init__(self,surname):
    self.surname = surname
    print(self.name)
    


me = Person ("Kvich")
you = Person ("Test")

print(me.age)
me.age += 1
print(me.age)

# print(me.surname)
# print(you.surname)