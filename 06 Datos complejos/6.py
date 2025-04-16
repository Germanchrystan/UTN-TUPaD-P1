signs = {"(":")", "{": "}", "[": "]"}

def isOpening(char: str) -> bool:
  return signs.keys().__contains__(char)

def isClosing(char: str) -> bool:
  return [")", "]", "}"].__contains__(char)

def checkBalance(data: str) -> bool:
  stack = []
  for i in range (0, len(data)):
    char = data[i]
    
    if isOpening(char):
      stack.append(char)
    
    if isClosing(char):
      if len(stack) == 0:
        return False
      
      lastStackItem = stack[len(stack) -1]
      if signs[lastStackItem] == char:
        stack.pop()
      else:
        return False
  return len(stack) == 0

firstCase = checkBalance("({{}})") # True
secondCase = checkBalance("({{}})()[]") # True
thirdCase = checkBalance("({{}})]") # False
fourthCase = checkBalance("[({{}})") # False

print(firstCase)
print(secondCase)
print(thirdCase)
print(fourthCase)
