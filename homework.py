# number from 1 to 1000000
num = 0

# longest chain here самая длинная цепочка здесь
maxLength = 0

# number that produce the longest chain число, создающее самую длинную цепочку
result = 0

while num < 1000000:
    num += 1
    k = num

    # count the current chain pieces подсчитайте текущие звенья цепи
    i = 0

    while k > 1:
        i += 1
        if k%2 == 0:
            k /= 2
        else:
            k = k*3 + 1

    if maxLength < i:
        maxLength = i
        result = num

print(result)