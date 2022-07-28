class student:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def tall(self):
        x=std[0]
        for i in range(1,n):
            if(x.height<std[i].height):
                x=std[i]
        print("The tallest is {0} age is {1} of the height {2}".format(x.name,x.age,x.height))
n=int(input("enter the number of students:"))
std=[]
for i in range(n):
    name=input()
    age=int(input())
    height=float(input())
    std.append(student(name,age,height))
for i in std:
  pass
i.tall()