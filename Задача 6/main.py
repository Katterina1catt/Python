# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

n=int(input("Введите номер билета: "))
a1=n//100000%10
a2=n//10000%10
a3=n//1000%10
b1=n//100%10
b2=n//10%10
b3=n%10
sum1=(a1+a2+a3)
sum2=(b1+b2+b3)
if sum1==sum2:
    print("У вас счастливый билет")
else:
    print("Ваш билет не выиграл")
