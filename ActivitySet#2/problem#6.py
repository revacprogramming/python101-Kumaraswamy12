
class Menu:
      def show(x):
        print(x.food,x.price)
      def add(x,food,price):
           x.food=food
           x.price=price
        


m = Menu()  # Menu is a class
m.show(add("idly", 10))
m.add("vada", 20)
m.show()



