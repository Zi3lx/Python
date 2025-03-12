#Zad 1-4
def pietro(znak):
    print(10 * znak)
    print(10 * znak)
    print(4 * znak + "00" + 4 * znak)
    print(4 * znak + "00" + 4 * znak)
    print(10 * znak)
    print(12 * znak)

def dach(znak):
    size = 5
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = znak + ' ' * (2 * (i - 1)) + znak
        print(spaces + stars)

def rysuj_dom(p, z1, z2):
    dach(z2)
    for i in range(p):
        pietro(z1)


rysuj_dom(0, "*", "%")


# Zad 5-6

def szukaj_w_liscie(lista, a) -> int:
    return lista.count(a)


print(szukaj_w_liscie([1,2,3,3,3,4,5,3], 3))
print(szukaj_w_liscie([1,2,3,3,3,4,5,3], True))


#Zad 7
from math import sqrt

def odleglosc(lista, lista2):
    return sqrt(((lista2[0]-lista[0]) ** 2) + ((lista2[1]-lista[1]) ** 2))


print(odleglosc([0,0],[0,4]))


#Zad 8

def obwodTrojkata(l1,l2,l3):
    return odleglosc(l1,l2) + odleglosc(l1,l3) + odleglosc(l2,l3)


print(obwodTrojkata([0,4], [4, 0], [4,4]))


#Zad 9-10
def wspoliniowe(l1,l2,l3):
    return (l2[0] - l1[0]) * (l3[1] - l1[1]) == (l3[0] - l1[0]) * (l2[1] - l1[1])


print(wspoliniowe([0,0], [1, 1], [2, 2]))


#Zad 11

import statistics

def info(lista):
    sr = sum(lista) / len(lista)
    med = statistics.median(lista)
    mi = min(lista)
    ma = max(lista)
    od = statistics.stdev(lista) if len(lista) > 1 else 0

    return("srednia " + str(sr) + " Mediana " + str(med) + " Min " + str(mi) + " Max " + str(ma) + " Od " + str(od))


print(info([1,2,3,4,5,6,7,8,6,4,3,3,45]))

#Zad 12
from collections import Counter

def czy_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

s1 = "babek"
s2 = "kebab"
print(czy_anagram(s1, s2))

#Zad 13
def sorting(lista, l):
    if l == 0:
        lista.sort()
    else:
        lista.sort(reverse=True)
    return lista


print(sorting([1,4,6,8,6,33,3,35,6,7,4,3,2], 0))
print(sorting([1,4,6,8,6,33,3,35,6,7,4,3,2], 1))

#Zad 14
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n // 2) + 1):
        if n % i == 0:
            return False
    return True


#Zad 15

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)

    res = 0
    for i in range(m):
        for j in range(n):
            curr = 0
            while (i + curr) < m and (j + curr) < n and s1[i + curr] == s2[j + curr]:
                curr += 1
            res = max(res, curr)

    return res

s1 = "AGGTAB"
s2 = "GXTXAYB"
print(lcs(s1, s2))


#Zad 16
def fibonacci(n: int):
    l1, l2 = 0, 1
    if n >= 1:
        print(l1)
    if n >= 2:
        print(l2)
    for i in range(2, n):
        l1, l2 = l2, l1 + l2
        print(l2)


print(fibonacci(5))

#Zad 17
def silnia(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans


print(silnia(5))

#Zad 18
def cel_to_far(n):
    f = (n * 9 / 5) + 32
    return f


print(cel_to_far(0), cel_to_far(100))

#Zad 19

def kwadrat(n):
    print(n * "* ")
    for i in range(n-2):
        print("* " + '  '*(n-2) + "* ")
    print(n * "* ")

    return n*n


print(kwadrat(10))

#Zad 20

def szyfr_cezara_encrypt(text, n):
    ans = ""
    for c in text:
        if c.isalpha():
            shift = ord(c) + n
            if c.islower():
                if shift > ord('z'):
                    shift -= 26
            elif c.isupper():
                if shift > ord('Z'):
                    shift -= 26
            ans += chr(shift)
        else:
            ans += c
    return ans


print(szyfr_cezara_encrypt("abcdABCD", 3))


#Zad 21

import random

word_list = ["apple", "grape", "mango", "pearl", "charm", "spike", "flame", "crisp", "drift"]

ans = random.choice(word_list)

attempts = 6

def check(guess, target):
    word = []
    for i, letter in enumerate(guess):
        if letter == target[i]:
            word.append(f"{letter.upper()}")  # Litera w dobrym miejscu
        elif letter in target:
            word.append(f"{letter.lower()}")  # Dobra litera złe miejsce
        else:
            word.append("_")
    return " ".join(word)

print(f"Zgadnij 5 literowe słowo po angielsku w {attempts} próbach.\n")

def play():
    for attempt in range(1, attempts + 1):
        guess = input(f"Próba {attempt}/{attempts}: ").lower()

        if len(guess) != 5 or not guess.isalpha():
            print("Podaj 5 literowe słowo")
            continue

        if guess == ans:
            print(f"Zgadłeś '{ans}' prawidłowo!")
            break

        feedback = check(guess, ans)
        print("Feedback: ", feedback)

        if attempt == attempts:
            print(f"Przegrałeś '{ans}'")

    print("Game Over.")

#play()

#Zad 22

def reverse_string(s) -> str:
    ans = ""
    for i in range(len(s)-1, -1, -1):
        ans += s[i]
    return ans

print(reverse_string("Ala ma kota"))

#Zad 23

class Person:
    def __init__(self, x, y):
        self.age = x
        self.imie = y

    def przedstaw_sie(self):
        return f"{self.imie} i mam {self.age} lat"


a = Person(10, "Andrzej")
print(a.przedstaw_sie())


#Zad 24
class Rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


rect = Rect(10, 15)
print(rect.area())


#Zad 25
class BankAccount:
    def __init__(self, balance):
        self.b = balance

    def withdraw(self, n):
        self.b = self.b - n
        return self.b

    def deposit(self, n):
        self.b = self.b + n
        return self.b


bank = BankAccount(1000)

print(bank.deposit(100))
print(bank.withdraw(100))


#Zad 26

class Student:
    def __init__(self):
        self.dziennik = {}

    def add_student(self, name):
        self.dziennik[name] = []

    def add_grade(self, name, grade):
        self.dziennik[name].append(grade)

    def students(self):
        for name, grades in self.dziennik.items():
            print(f"Student: {name}, Oceny: {grades}")


students = Student()

students.add_student("Jan Kowalski")
students.add_grade("Jan Kowalski", 5)
students.add_grade("Jan Kowalski", 4)

students.add_student("Anna Nowak")
students.add_grade("Anna Nowak", 3)

students.students()


#Zad 27

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add_dis(self, procent):
        self.price -= self.price * procent
        return self.price


p = Product("A", 100)
print(p.add_dis(0.1))

#Zad 28
class User:
    def __init__(self):
        self.rejestr = {}

    def register(self, login, password):
        if login not in self.rejestr:
            self.rejestr[login] = password

    def login(self):
        l = input("Login")
        p = input("Password")

        if l in self.rejestr:
            if self.rejestr[l] == p:
                return "Zalogowany"

        return "Błąd"

    def print_all(self):
        for log, pas in self.rejestr.items():
            print(f"Login: {log}, Password: {pas}")


u = User()
u.register("ala", "haslo")
print(u.login())

