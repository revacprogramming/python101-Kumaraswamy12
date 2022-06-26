import math
def process():
  x1,y1,x2,y2,x3,y3=map(float,input().split())
  area=(math.sqrt((x3-x2)**2+(y3-y2)**2))*(math.sqrt((x2-x1)**2+(y2-y1)**2))
  print(f"Area of rectangle with vertices ({x1},{y1}),({x2},{y2}),({x3},{y3}) is {area}" )
def main():
  a=int(input("enter the number of rectangles:"))
  for i in range(a):
      process()

main()
#try solving in proper way

    
