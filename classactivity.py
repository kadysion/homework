#question 1

# a = int(input("Enter an integer 1:"))
# b = int(input("Enter an integer 2:"))
#
# if a > b:
#     print("True")
# else:
#     print("False")

# question 2

# a = int(input("Enter an integer 1:"))
# b = int(input("Enter an integer 2:"))
# c = int(input("Enter an integer 3:"))
#
# if (a + b) > c:
#     print("True")
# else:
#     print("False")

# question 3

# a = int(input("Enter the number: "))
#
# if a / 2:
#     print("True")
# else:
#     print("False")

# question 4

# num = int(input("Enter the number: "))
#
# if num == 0 and num / 2:
#     print("True")
# else:
#     print("False")

# question 5

# num = int(input('Enter the number from 1 to 7:'))
#
# if num == 6 and num == 7:
#     print("Weekend")
# elif num >= 1 and num < 6:
#     print("Weekday")
# else:
#     print("Invalid unput.")


# question 1b

# num = int(input("Enter an integer: "))
#
# if num > 20:
#     num /= 6
# else:
#     num *= 6
#
# print(num)

# question 2b
#
# num = int(input("Enter an integer: "))
#
# if num > 0:
#     num += 1
# elif num < 0:
#     num -= 2
# else:
#     num = 10
#
# print(num)

# question 3b

# a = int(input("Enter an integer 1: "))
# b = int(input("Enter an integer 2: "))
#
# if a != b:
#     print(a, b)
# else:
#     a = 0
#     b = 0
#
# print(a, b)

# question 4b

# num = int(input("Enter an integer: "))
#
# if num > 0:
#     num += 1
# else:
#     num = 0
#
# print(num)

# question 5b

# a = int(input("Enter an integer 1:"))
# b = int(input("Enter an integer 2:"))
#
# if a % b:
#     print("Not divisible")
# else:
#     print("Divisible")

# if, else, elif

# question 1

# a = int(input("Сколько рекомендуется спать?"))
# b = int(input("Не стоит спать более:"))
# h = int(input("Сколько часов спит Аня?"))
#
# if h > b:
#     print("Пересып.")
# elif h < a:
#     print("Недосып.")
# else:
#     print("Это норма.")

# question 2

# year = int(input("Enter the year (from 1900 to 3000): "))
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Leap year")
# else:
#     print("Usual year")

# question 3
#
# num = int(input("Enter a number: "))
#
# if -15 <= num <= 12 or 14 <= num <= 17 or num >= 19:
#     print("True")
# else:
#     print("False")

# question 4

# pi = 3.14
#
# figure = input("Введите тип фигуры: ")
#
# if figure == "треугольник":
#     a = int(input("Введите сторону a:"))
#     b = int(input("Введите сторону b:"))
#     c = int(input("Введите сторону c:"))
#
#     p = (a + b + c)/2
#     S = p + p
#     print(S)
#
# elif figure == "прямоугольник":
#     a = int(input("Введите сторону a:"))
#     b = int(input("Введите сторону b:"))
#
#     S = a * b
#     print(S)
#
# elif figure == "круг":
#     r = int(input("Введите радиус:"))
#
#     S = pi * r**2
#     print(S)
#
# else:
#     print("Неверная фигура.Попробуйте еще раз.")

# question 5

# num = int(input("Введите число программистов: "))
#
# if num % 10 == 1 and num % 100 != 11:
#     ending = "программист"
# elif 2 <= num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
#     ending = "программиста"
# else:
#     ending = "программистов"
#
# print(f"{num} {ending}")

# homework 4

# question 1

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
#
# if a + b > c and a + c > b and b + c > a:
#     print("True")
# else:
#     print("False")

# question 2

# a = int(input("Введите число a: "))
#
# if a % 2 == 0:
#     print("True")
# else:
#     print("False")

# question 3

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
#
# if a + b > c:
#     print("True")
# else:
#     print("False")

# question 4

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
#
# if a > b:
#     print("True")
# else:
#     print("False")

# условный оператор

# question 1

# login = input("Enter your login: ")
# password = input("Enter your password: ")
#
# if login == "user" and password == "qwerty":
#     print("Authentication completed.")
# else:
#     print("Invalid login or password.")

# question 2

# kzt = int(input("Enter amount in KZT: "))
# print("Выберите валюту:")
# print("[1] USD")
# print("[2] EUR")
# print("[3] RUB")
# choice = input("Choose currency:")
#
# if choice == "1":
#     rate = kzt / 420
#     currency = "USD"
# elif choice == "2":
#     rate = kzt / 510
#     currency = "EUR"
# elif choice == "3":
#     rate = kzt / 5.8
#     currency = "RUB"
# else:
#     print("Invalid input.Try again.")
#
# print(f"{rate:.2f} {currency}")

# блоки в python

# s = int(input("Стоимость подписки на онлайн-кинотеатр: "))
# p = int(input("Стоимость пиццы: "))
# m = int(input("Зарплата:"))
#
# if s + p <= m:
#     print("Да")
# else:
#     print("Нет")

# условия в python

ticket_number = input("Введите номер билета (шестизначное число): ")


if len(ticket_number) == 6 and ticket_number.isdigit():
    first_half = list(map(int, ticket_number[:3]))
    second_half = list(map(int, ticket_number[3:]))


    if sum(first_half) == sum(second_half):
        print("Счастливый")
    else:
        print("Обычный")
else:
    print("Invalid input.Enter a correct number.")

