total = 0
count = 0
avarage = 0
max_number = 0
min_number = 0
even = 0
odd = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a != 0:
        total += a
        count += 1
        avarage = total / count
    if a > max_number:
        max_number = a
    if a < min_number or min_number == 0:
        min_number = a
    if a % 2 == 0:
        even += 1
    if a % 2 == 1:
        odd += 1
print('Общее количество:', count)
print('Cумма всех чисел:', total)
print('Среднее арифметическое:', avarage)
print('Максимальное число:',max_number)
print('Минимальное число:',min_number)
print('Количество четных:',even)
print('Количество не четных:',odd)


