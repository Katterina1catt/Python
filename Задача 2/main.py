# Найдите сумму цифр трехзначного числа

n=int(input("Введите трехзначное число: "))
if 99<n<1000: 
    a=n//100%10
    b=n//10%10
    c=n%10
    sum=(a+b+c)
    print(int(sum))
else:
    print("Введите другое число")