L = [1, 2, 3, 4, 5]
fun1(x):
  return lambda: x * x
  
  
fun2():
  return lambda x: x * x

R = map(fun1, L)
for i in R:
  print(i())

R = map(fun2(), L)
  for i in R:
  print(i)
