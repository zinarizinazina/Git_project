## Задача 2

a = int(input()) # пятизначное число
b = (a // 10000) 
c = (a - b * 10000) // 1000
d = (a - b * 10000 - c * 1000) // 100
e = (a - b * 10000 - c * 1000 - d * 100) // 10
f = (a - b * 10000 - c * 1000 - d * 100 - e * 10) // 1
print (b, c, d, e, f)
R1 = e ** f
R2 = R1 * d
if b != c :
    R = R2 / (b - c)
    print(R)
else:    
    print('Деление на 0 невозможно')
