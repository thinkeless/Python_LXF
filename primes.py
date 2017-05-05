def odd():
    n = 1
    while True:
        n += 2
        yield n
        
        
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
        
for s in primes():
    if s < 50:
        print(s)
    else:
        break
        
        
#200到300之间的素数
result = []
for i in range(200, 301):
    r = 0
    for n in range(1, i+1):
        if i % n == 0:
            r += 1
    if r == 2:
        result.append(n)

print(result)
