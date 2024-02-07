test_1 = 37
test_2 = [12, 14, 99]

print(f'{test_1=}')
print('test_2 is', test_2)

def doubler(x):
    y = x * 2
    return y

print(doubler(test_1))
print(doubler(test_2))

class Wrapper:
    def __init__(self, x):
        self.x = x
    def tripler(self):
        y = self.x * 3
        return y

w1 = Wrapper(test_1)
w2 = Wrapper(test_2)

print(w1.tripler())
print(w2.tripler())