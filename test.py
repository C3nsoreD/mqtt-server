import random, string


def data():
    values = {}
    count = 0
    
    while count < 10:
        value1 = int(random.randint(1, 100))
        value2 = [''.join(random.choice(string.ascii_letters) for _ in range(3))]
        values[value1] = value2
        count += 1

    return values

print(data())