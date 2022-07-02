def input_set():
  set=(input('Enter Set  : ')).split(' ')
  return set

def get_operation():
  operation =input('enter the operation to be done  (u/n):')
  return operation
  
def get_operands():
  x=[]
  operands=(input('enter the operands (s1/s2/s3) :')).split(' ')
  for i in operands :
    if i=="s1":
      x.append(set1)
    elif i=="s2":
      x.append(set2)
    else:
      x.append(set3)

  return x

def perform_operation(operation,*operands):
  if operation  == 'u':
      s4=operands[0]
      for ele in operands[1]:
        if ele not in s4:
          s4.append(ele)
      s4.sort()

      if len(operands)>=3:
        s5=s4
        for ele in operands[2]:
          if ele not in s4:
            s5.append(ele)
        return s5 
      return s4
  elif operation == 'n':
    s4 = []
    for ele in operands[0]:
      if ele in operands[1]:
        s4.append(ele)
    s4.sort()

    if len(operands)>=3:
      s5 = []
      for ele in operands[2]:
        if ele in s4:
          s5.append(ele)

      return s5
    return s4

  

def main():
    global set1 ,set2, set3
    # setu = input_set()
    set1 = input_set()
    set2 = input_set()
    set3 = input_set()
    
    operation = get_operation()
    operands = get_operands()
    print(operands)
    result =perform_operation(operation,*operands)
    print(result)
    # print_report(setu,set1,set2,set3) # members in only s1 and s2, members in only s2,s3, members in only s3,s1, members not in s1,s2,s3 and members in all s1,s2,s3 ... question given 
main()