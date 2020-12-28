from math import gcd

def solution(n):
  out = 0
  for k in range(1, n + 1):
    out += k * k * phi(k) * (n // k) * (n // k + 1) // 2
  return out

def solution_facile(k):
  sum = 0
  for i in range(1, k + 1):
    for j in range(1, k + 1):
      sum += ppcm(i, j)
  return sum

def factor(n):
  if n == 1:
    return {1: 1}
  out = {}
  i = 2
  while n > 1:
    while n % i == 0:
      if i not in out.keys():
        out[i] = 0
      out[i] += 1
      n = n // i
    i = i + 1
  return out

def divisors(n):
  from functools import reduce
  factors = list(factor(n).items())
  nfactors = len(factors)
  f = [0] * nfactors
  while True:
    yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
    i = 0
    while True:
      f[i] += 1
      if f[i] <= factors[i][1]:
        break
      f[i] = 0
      i += 1
      if i >= nfactors:
        return

def ppcm(i, j):
  return i * j // gcd(i, j)

def phi(k):
  if k == 1:
    return 1
  out = k
  for i in factor(k).keys():
    out = out * (i - 1) // i
  return out

def lcmsum(k):
  out = 2
  for d in factor(k).keys():
    out += d * phi(d)
  out = out * k // 2
  return out

if __name__ == "__main__":
  import time
  start = time.time()

  ## Put code to measure time here

  end = time.time()
  print(end - start)
