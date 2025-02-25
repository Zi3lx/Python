#__________Zad 13__________
a = input("Podaj cos 1\n")
b = input("Podaj cos 2\n")

if a == b:
    print("YES")
else:
    print("NO")


#__________Zad 14__________
x = input("Podaj liczbe\n")

if int(x) % 2 == 0:
    print("Tak parzysta")
else:
    print("Nie, nie jest parzysta")


#__________Zad 15__________
x = input("Podaj liczbe\n")

try:
    help = eval(x)

    if isinstance(help, bool):
        print("bool")
    elif isinstance(help, float):
        print("float")
    elif isinstance(help, int):
        print("int")
    else:
        print("string")
except:
    print("string")


#__________Zad 16__________
a = int(input("Podaj cos 1\n"))
b = int(input("Podaj cos 2\n"))

if a >= b:
    print(a)
else:
    print(b)


#__________Zad 17__________
a = int(input("Podaj cos 1\n"))
b = int(input("Podaj cos 2\n"))
c = int(input("Podaj cos 3\n"))

big = a

if b > big:
    big = b

if c > big:
    big = c

print(big)


#__________Zad 18__________
a = int(input("Podaj cos 1\n"))
b = int(input("Podaj cos 2\n"))
c = int(input("Podaj cos 3\n"))

tab = [a,b,c]

tab.sort()

print(tab)


#__________Zad 19__________
a = int(input("Podaj a\n"))
b = int(input("Podaj b\n"))

if b != 0 and a == 0:
    print("0 miejsc")
elif a == 0 and b == 0:
    print("duzo")
else:
    print(-b/a)


#__________Zad 20__________
a = int(input("Podaj cos 1\n"))
b = int(input("Podaj cos 2\n"))
c = int(input("Podaj cos 3\n"))

delta = b * b - 4 * a * c

if delta > 0:
    print("2 miejsca zerowe")
elif delta == 0:
    print("1 miejsce zerowe")
else:
    print("Nie ma")

#__________Zad 21__________
a = int(input())
j = a % 10
d = (a // 10) % 10
s = (a // 100) % 10
print("Setki: " + str(s) + ", Dziesiatk: " + str(d) + ", Jednosci: " + str(j))