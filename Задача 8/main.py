# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).

m=int(input("Введите ширину шоколадки: "))
n=int(input("Введите длину шоколадки: "))
k=int(input("Введите количество долек: "))
if m*n<k and (k%n==0 or k%m==0):
    print("Yes")
else:
    print("No")