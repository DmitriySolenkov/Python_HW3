num = int(input('Введите число: '))
array = []
while num != 1:
    array.append(int(num % 2))
    num = int(num/2)
array.append(1)
string = ""
for j in range(len(array)):
    string += str(array[-j-1])
print(string)
