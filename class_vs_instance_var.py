class car:
  
  wheel = 4
  def __init__(self,name,milage):
    self.name = name
    self.milage = milage

c1 = car('BMW','18')
c2 = car('Audi','21')

print(c1.name, c1.milage, c1.wheel) # prints BMW 18 4

c2.milage = 24
print(c2.name, c2.milage, c1.wheel) # prints Audi 24 4

# Now what if we want to change wheels can an object do that ? NO! wheel is a class variable and not an instance variable.
# An instance variables are avriable that belongs to object in this case milage and name are instance variable.
# So to change wheels to let say 5 we need to change it using class name
# class method is same as static method

car.wheel = 5

#Now if we again print the values this time wheels for all the objects will change to 5

print(c1.name, c1.milage, c1.wheel) # prints BMW 18 5

c2.milage = 24
print(c2.name, c2.milage, c1.wheel) # prints Audi 24 5
