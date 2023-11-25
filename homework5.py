# class work 

# question1

# base = 2
# power = 0

# while power <= 20:
#     result = base ** power
#     print(f"{result}")
#     power += 1


# question3

# total = 0
# while True:
#     num = int(input("Enter the number: "))
#     if num == 0:
#         break
#     total += num
# print(f"Total of all numbers: {total}")


# for 

# question1

# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))

# print("All numbers in range: ")
# for num in range(start,end + 1):
#     print(num, end=" ")
# print("\n")

# print("All odd numbers in range: ")
# for num in range(start, end + 1):
#     if num % 2 != 0:
#         print(num, end=" ")
# print("\n")

# print("All even numbers in range: ")
# for num in range(start, end + 1):
#     if num % 2 == 0:
#         print(num, end=" ")
# print("\n")

# print("All numbers in range in decreasing order: ")
# for num in range(end, start -1, -1):
#     print(num, end=" ")
# print("\n")


# question2

# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# c = int(input("Enter the number: "))
# d = int(input("Enter the number: "))

# print('\t', end='')
# for i in range(c, d + 1):
#     print(i, end='\t')
# print()

# for i in range(a, b + 1):
#     print(i, end='\t')  
#     for j in range(c, d + 1):
#         print(i * j, end='\t')  
#     print()  

# циклы

# question1

# for i in range(1,6,1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# for i in range(6,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# question2

# while True:
#     num = int(input("Enter an integer: "))
#     if num < 10:
#         continue
#     elif num >100:
#         break
#     else:
#         print(num)

# question3

# def sum_of_divisors(n):
#     divisors_sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             divisors_sum += i
#     return divisors_sum

# print("Numbers from 1 to 100:")
# for num in range(1, 101):
#     if num == sum_of_divisors(num):
#         print(num)

    
# homework5

# a = int(input("Enter number of participants in group a: "))
# b = int(input("Enter number of participants in group b: "))

# d = max(a, b)
# while d % a != 0 or d % b != 0 :
#     d += 1

# print(d)

# for

# question1
# n = int(input("Enter the number: "))

# factorial = 1
# sum_factorials = 0

# for i in range(1, n + 1):
#     factorial *= i
#     sum_factorials += factorial

# print(f"Sum of numbers{n}: {sum_factorials}")

# question 2
# n = int(input("Enter the number, number <= 9: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()

# циклы

# question1

# n = int(input("Enter the total number of cards: "))  

# remaining_numbers = list(map(int, input(f"Enter {N - 1} numbers of the remaining cards: ").split()))  

# sum_all = (n * (n + 1)) // 2
# sum_remaining = sum(remaining_numbers)
# missing_card = sum_all - sum_remaining

# print(missing_card)

#question2

# n = int(input("Enter the number: "))

# sqrt_n = int(N ** 0.5)


# for i in range(1, sqrt_n + 1):
#     square = i * i
#     if square <= n:
#         print(square)
#     else:
#         break







