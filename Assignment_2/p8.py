class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        number = self.current
        self.current += 1
        return number


n = int(input("Enter n: "))
numbers = NumberIterator(n)

for number in numbers:
    print(number)