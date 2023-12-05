# question 1

# import math

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print("Available operations:")
# print("1. Addition ")
# print("2. Subtraction ")
# print("3. Multiplication ")
# print("4. Division ")
# print("5. Exponentiation ")
# print("6. Factorial ")
# print("7. Fibonacci Number ")
# print("8. Sine ")
# print("9. Cosine ")
# print("10. Tangent ")

# operation = input("Select an operation : ")

# if operation in ('1', '2', '3', '4', '5'):
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
    
#     if operation == '1':
#         result = num1 + num2
#     elif operation == '2':
#         result = num1 - num2
#     elif operation == '3':
#         result = num1 * num2
#     elif operation == '4':
#         result = num1 / num2
#     elif operation == '5':
#         result = num1 ** num2
#     print(f"Result: {result}")
    
# elif operation == '6':
#     num = int(input("Enter a number to calculate its factorial: "))
#     print(f"The factorial of {num}: {factorial(num)}")
    
# elif operation == '7':
#     num = int(input("Enter the position of the Fibonacci number: "))
#     print(f"The Fibonacci number at position {num}: {fibonacci(num)}")
    
# elif operation in ('8', '9', '10'):
#     angle = float(input("Enter the angle in degrees: "))
#     if operation == '8':
#         result = math.sin(math.radians(angle))
#         print(f"The sine of {angle}°: {result}")
#     elif operation == '9':
#         result = math.cos(math.radians(angle))
#         print(f"The cosine of {angle}°: {result}")
#     elif operation == '10':
#         result = math.tan(math.radians(angle))
#         print(f"The tangent of {angle}°: {result}")
# else:
#     print("Invalid operation.")

# question 2

# def print_board(board):
#     print("-------------")
#     for i in range(0, 9, 3):
#         print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
#     print("-------------")

# def check_winner(board, player):
#     win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
#             return True
#     return False

# def tic_tac_toe():
#     print("********** Tic tac toe **********")
#     board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     current_player = 'X'
#     while True:
#         print_board(board)
#         move = input(f"Where do you want to put{current_player}? ")
#         if board[int(move) - 1] not in ['X', 'O']:
#             board[int(move) - 1] = current_player
#             if check_winner(board, current_player):
#                 print_board(board)
#                 print(f"{current_player} won!")
#                 break
#             elif all([cell == 'X' or cell == 'O' for cell in board]):
#                 print_board(board)
#                 print("Draw!")
#                 break
#             current_player = 'O' if current_player == 'X' else 'X'
#         else:
#             print("Place is taken. Try again.")

# tic_tac_toe()

# question3

# from collections import Counter

# def determine_winner(votes):
#     vote_count = Counter(votes)
#     max_votes = max(vote_count.values())
    
#     winners = [candidate for candidate, count in vote_count.items() if count == max_votes]
    
   
#     if len(winners) > 1:
#         winners = sorted(winners, key=lambda x: len(x))
    
#     winner = winners[0]
#     winner_votes = vote_count[winner]
    
#     return winner, winner_votes

# votes = ['Candidate A', 'Candidate B', 'Candidate A', 'Candidate C', 'Candidate A', 'Candidate B', 'Candidate C']

# winner, winner_votes = determine_winner(votes)
# print(f"Winner: {winner} : {winner_votes}")
