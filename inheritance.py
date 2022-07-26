class A:
  def __init__(self):
    print('in A')
  
  def feature1 (self):
    print('feature 1 from A')

class B:
  def __init__(self):
    print('in B')
  
  def feature1 (self):
    print('feature 1 from B')

class C(A,B):
  def __init__(self):
    print('in C')
    super().__init__() # The output of this will be 'in A' This is due to method resolution order which is from left to right.
    

c1 = C() # will print in C and in A
c1.feature1() # this will print feature 1 from A since A appears before B in ingeritance (MRO).
  
