class school:
  school_name = 'BCM'
  
  # This is instance method
  def __init__(self,math,science):
    self.math = math
    self.science = science
   
  # This is how we define class method, using decorators
  @classmethod
  def info(cls):
    print(cls.school_name)
   
  
  # Now lets say you want a function that do square of a number that has nothis to do with this class in this case we will create static method
  # For static method we need to use @staticmethod decorator
  @staticmethod
  def square(n):
    return n*n
    
