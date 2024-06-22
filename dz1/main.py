# num_1 = int(input("Enter your first num --> "))
# num_2 = int(input("Enter your second num --> "))
# n = 0
# sum_odd = 0
# sum_even = 0
# sum_9 = 0
# if num_1 > num_2:
#     for i in range(num_2, num_1, 1):
#         if i % 2 != 0:
#             n += 1
#             sum_odd = sum_odd + i
#     else:
#         print(f"the sum of odd numbers = {sum_odd}")
#         print(f"Ar = {sum_odd/n}")
#     for i in range(num_2,num_1,1):
#         if i % 2 == 0:
#             n += 1
#             sum_even = sum_even + i
#             print(sum_even, i)
#     else:
#         print(f"the sum of even numbers = {sum_even}")
#         print(f"Ar = {sum_even/n}")
#     for i in range(num_2, num_1, 1):
#         if i % 9 == 0:
#             n += 1
#             sum_9 = sum_9 + i
#     else:
#         print(f"The sum = {sum_9}")
#         print(f"Ar = {sum_9/n}")
# if num_2 > num_1:
#     for i in range(num_1, num_2, 1):
#         if i % 2 != 0:    
#             n += 1
#             sum_odd = sum_odd + i
#     else:
#         print(f"the sum of odd numbers = {sum_odd}")
#         print(f"Ar = {sum_odd/n}")
#     for i in range(num_1,num_2,1):
#         if i % 2 == 0:
#             n += 1
#             sum_even = sum_even + i
#     else:
#         print(f"the sum of even numbers = {sum_even}")
#         print(f"Ar = {sum_even/n}")
#     for i in range(num_1, num_2, 1):
#         if i % 9 == 0:
#             n += 1
#             sum_9 = sum_9 + i
#     else:
#         print(f"The sum = {sum_9}")
#         print(f"Ar = {sum_9/n}")

# width = int(input("enter width --> "))
# symbol = str(input("enter symbol --> "))
# for i in range(1, width, 1):
#     print(symbol)
# else:
#     print(symbol)

# isFinished = False
# while(isFinished == False):    
#     num = int(input("enter your num (Enter 7 to finish) --> "))
#     if num > 0 and num != 7:
#         print(f"{num} is positive")
#     elif num < 0 and num !=7:
#         print(f"{num} is negative")
#     elif num == 0:
#         print(f"{num} is equal to zero")
#     else:
#         print("Good bye!")
#         isFinished = True

min = 0
max = 0
sum = 0
isFinished = False
while(isFinished == False):
    num = int(input("Enter your num (Enter 7 to finish) --> "))
    num1 = num
    min = 100000000000000000000000000000000000000000000000000000000000000000000001
    if num == 7:
        print("Good bye!")
        isFinished = True
    if num < min and num != 7:
        min = num1
    if num > max and num != 7:
        max = num1
    if num != 7:    
        sum = sum + num
else:
    print(f"Sum = {sum}\nMax = {max}\nMin = {min}")
     
