x = int(input("숫자?: "))

i = 2
while i == 2:
    if x%i == 0:
        print(i, end=' ')
        x = x / i
        continue
    else:
        i += 1
while i <= x:
    if x%i == 0:
        print(i, end=' ')
        x = x / i
        continue
    i += 2
