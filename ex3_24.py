def f(r, gamma, it):
  v = 0.0
  k = 1.0
  for i in range(0, it):
    l = 0.0
    if i % 5 == 0:
      l = r
    v += k * l
    k = k * gamma
  return v

for i in range(1, 1000):
  print("i: " + str(i) + " -> " + str(f(10, 0.9, i)))
