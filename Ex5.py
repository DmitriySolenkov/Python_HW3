num = int(input('Введите количество чисел Фибоначчи: '))
arrayPos = [0, 1]
arrayNeg = [-1]
arraySum = []
if num > 0:
    if num > 1:
        for i in range(num-1):
            arrayPos.append(arrayPos[i]+arrayPos[i+1])
            if i % 2 == 0:
                arrayNeg.insert(0, -arrayPos[i+2])
            else:
                arrayNeg.insert(0, arrayPos[i+2])
    arraySum = arrayNeg
    for j in range(len(arrayPos)):
        arraySum.append(arrayPos[j])
    print(arraySum)
else:
    print('Неверное число!')
