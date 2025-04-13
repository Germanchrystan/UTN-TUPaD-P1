# "()", "{}", "[]"
openingSigns = {"(":")", "{": "}", "[": "]"}

def checkBalance(data):
  stack = []
  balanced = True
  for i in range (0, len(data)):
    char = data[i]
    if openingSigns.keys().__contains__(char):
      stack.append(char)
      for j in range (i, len(data)):

"({{}})"
