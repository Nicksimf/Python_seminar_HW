# Задача 2: Найдите сумму цифр трехзначного числа.

# 1 вариант
n = input()
print(int(n[0])+int(n[1])+int(n[2]))

# 2 вариантgit
n = int(input())
z = n % 10
x = n // 100
c = (n // 10) % 10
print(z+x+c)

# Задача 4. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

summ=int(input())
p = int(input())
s = p
k = (p + s)*2
print(p,k,s)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

n = input()
if (int(n[0])+int(n[1])+int(n[2])) == (int(n[3])+int(n[4])+int(n[5])):
    print('lucky')
else:
    print('unlucky')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input())
m = int(input())
k = int(input())
if k < m*n and (k%m==0 or k%n==0):
    print('Можно')
else:
    print('Нельзя')