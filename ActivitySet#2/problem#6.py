
class Menu:
  def add(x,food,price):
           x.food=food
           x.price=price
  def show(x):
        print(x.food,x.price)
      


  
m = Menu()
m.add("idly", 10)# Menu is a class
m.show()
m.add("vada", 20)
m.show()




