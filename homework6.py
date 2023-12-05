# homework

# question 1

# def count_odd_even(numbers):
#     odd_count = sum(1 for num in numbers if num % 2 != 0)
#     even_count = sum(1 for num in numbers if num % 2 == 0)
   
    
#     if odd_count > even_count:
#         return "No"
#     else:
#         return "Yes"


# N = 10
# user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# result = count_odd_even(user_list)
# print(result)

# question 2

# def create_nested_list():
#     nested_list = []  
#     for i in range(3):
#         inner_list = []  
#         for j in range(3):
#             inner_list.append(int(input(f"Enter the numbers: ")))  
#         nested_list.append(inner_list)  
#     return nested_list

# def sum_diagonal(matrix):
#     diagonal_sum = 0
#     for i in range(len(matrix)):
#         diagonal_sum += matrix[i][i]  
#     return diagonal_sum

# matrix = create_nested_list()

# print("Create the list:")
# for row in matrix:
#     print(row)

# diagonal_sum = sum_diagonal(matrix)
# print(f"Sum of numbers:: {diagonal_sum}")

# question 3

# def cv_program():
#     print("Enter your personal deatails: ")
#     name = input("Enter your name: ")
#     surname = input("Enter your surname: ")
#     address = input("Enter your address: ")
#     email = input("Enter your email address: ")
#     profile = input("Enter your Linkedin profile: ")
#     portfolio = input("Enter your account name: ")

#     cv_data = {
#         "First name": name,
#         "Surname": surname,
#         "Address": address,
#         "Email address": email,
#         "Linkedin profile": profile,
#         "Twitter/blog/portfolio": portfolio

#      }
#     return cv_data

# user_cv = cv_program
# print("/nEntered data for CV:")
# print(user_cv)

# functions

# question1 

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# def print_fibonacci_sequence(n):
#     for i in range(1, n+1):
#         result = fibonacci(i)
#         print(f"fibonacci number {i} = {result}")

# count = 10
# print_fibonacci_sequence(count)


# question2

# def is_power_of_two(n):
#     return n > 0 and (n & (n - 1)) == 0

# number = int(input("Enter the number: "))
# result = is_power_of_two(number)

# print(f"Number {number} is the power of two: {result}")
