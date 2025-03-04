#Zad 1
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n // 2) + 1):
        if n % i == 0:
            return False
    return True


def prime_selector(numbers: list[int]) -> list[int]:
    ans = []
    for number in numbers:
        if isPrime(number):
            ans.append(number)
    return ans


test = [1, 2, 3, 4, 10, 15, 17, 21, 23]
print(prime_selector(test))


#Zad 2

def round_numbers(numbers: list[int], threshold: int) -> list[int]:
    result = []
    for number in numbers:
        if number < threshold:
            result.append(number - (number % 10))
        else:
            result.append((number + 9) // 10 * 10)
    return result


numbers = [21, 37, 47, 15, 19, 41]
threshold = 30
print(round_numbers(numbers, threshold))


#Zad 3
def longest_increasing_subsequence(sequence: list[int]):
    maxx = 1
    help = 1
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            help += 1
            maxx = max(maxx, help)
        else:
            help = 1
    return maxx


test = [1, 2, 3, 4, 50, 15, 17, 21, 23]
print(longest_increasing_subsequence(test))

#Zad 4
def is_balanced(expression: str) -> bool:
    tab = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "{}()[]":
            tab.append(char)

    if len(tab) % 2 != 0:
        return False

    i = 0
    while i < len(tab):
        if i + 1 < len(tab) and tab[i] in "({[" and tab[i + 1] in ")}]":
            if tab[i + 1] == ')' and tab[i] != '(':
                return False
            if tab[i + 1] == ']' and tab[i] != '[':
                return False
            if tab[i + 1] == '}' and tab[i] != '{':
                return False

            del tab[i:i + 2]
            i = max(i - 2, 0)
        else:
            i += 1

    return len(tab) == 0


print(is_balanced("()"))
print(is_balanced("([]{})"))
print(is_balanced("(]"))
print(is_balanced("([)]"))
print(is_balanced("{[()]}"))

#Zad 5
def transposition_cipher(text: str, key: int) -> str:
    if key > len(text):
        return text

    result = list(text)

    for i in range(key-1, len(text), key-1):
        if i + key - 1 < len(text):
            result[i], result[i + key - 1] = result[i + key - 1], result[i]

    return ''.join(result)


text="abcdefghij"
print(transposition_cipher(text, 3))

#Zad 6
def fibonacci_generator(n: int):
    l1, l2 = 0, 1
    if n >= 1:
        print(l1)
    if n >= 2:
        print(l2)
    for i in range(2, n):
        l1, l2 = l2, l1 + l2
        print(l2)


print(fibonacci_generator(10))


#Zad 7
def most_frequent_element(data: list):
    map = {}

    for i in data:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    most_frequent = max(map, key=map.get)

    return most_frequent


data = [1, 2, 3, 2, 1, 2, 4, 4, 4, 2, 1, 1, 1]
print(most_frequent_element(data))

#Zad 8

def wskaznik_czytelnosci(tekst: str) -> float:
    zdania = tekst.split(".")
    zdania = [s.strip() for s in zdania if s.strip()]

    if not zdania:
        return 0.0

    liczba_slow_na_zdanie = [len(s.split()) for s in zdania]
    srednia_slow_na_zdanie = sum(liczba_slow_na_zdanie) / len(zdania)

    slowa = tekst.lower().split()
    if not slowa:
        return 0.0

    liczba_sylab = [policz_sylaby(slowo) for slowo in slowa]
    srednia_sylab_na_slowo = sum(liczba_sylab) / len(slowa)

    wynik = (srednia_slow_na_zdanie + srednia_sylab_na_slowo) / 2
    return wynik

def policz_sylaby(slowo: str) -> int:
    samogloski = "aeiouy"
    licznik = 0
    poprzednia_samogloska = False

    for znak in slowo:
        if znak in samogloski:
            if not poprzednia_samogloska:
                licznik += 1
            poprzednia_samogloska = True
        else:
            poprzednia_samogloska = False

    if slowo.endswith("e"):
        licznik -= 1

    return max(1, licznik)

# Przykład użycia
tekst = "To jest przykładowy tekst. Składa się z kilku zdań. Czy jest wystarczająco czytelny?"
wynik = wskaznik_czytelnosci(tekst)
print(f"Wskaźnik czytelności: {wynik}")


#Zad 9
import itertools

def unique_permutations(elements: list):
    permutacje = itertools.permutations(elements)
    return [list(perm) for perm in set(permutacje)]


elements = [1, 2, 2]
print(unique_permutations(elements))


#Zad 10
def group_words_by_length(words: list[str]):
    slownik = {}

    for word in words:
        slownik.setdefault(len(word), []).append(word)

    return slownik


words = ["ala", "ma", "kota", "a", "kot", "ma", "ale"]
print(group_words_by_length(words))



