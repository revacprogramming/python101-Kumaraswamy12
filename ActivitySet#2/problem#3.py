def get_cs():
    return(input())
def cs_to_lot(cs):
  y=[]
  lt=cs.split(';')
  for i in lt:
      x=(i.split("="))
      y.append(tuple(x))
  return y
def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)

main()
