
def add(a, b):
  return(a+b)
  pass
def output(a, b, sum):
  print(f'{a}+{b} is {sum}')
  pass
def main():
  a,b= [int(input('INPUT?')),int(input())]
  sum = add(a,b)
  output(a, b, sum)
main()
