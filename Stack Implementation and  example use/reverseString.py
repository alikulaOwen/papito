from stack import Stack

def reverseString(stack,input_str):
  for i in range(len(input_str)):
    stack.push(input_str[i])
  rev_str = ""
  while not stack.is_empty():
    rev_str+= stack.pop()

  return rev_str

  stack= Stack()
  input_str = input("Enter Your string: ")
  print(reverseString(stack,input_str))