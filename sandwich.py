def bread(func):
  def wrapper():
      print(" </''''''''\> ")
      func()
      print(" <\________/> ")
  return wrapper
 
def vegetables(func):
  def wrapper():
      print("---#tomato#---")
      func()
      print("~lettuce leaf~")
  return wrapper
 
def sandwich1(food="--====ham====-"):
  print(food)
 
sandwich = bread(vegetables(sandwich1))
sandwich()

@bread
@vegetables
def sandwich2(food="--===bacon===-"):
  print(food)
 
sandwich2()
