"""
Problem:
FizzBuZZ

Difficulty:
Easy

Approach:
Math, String

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

n = int(input("Enter the range for FizzBuzz"))
answer=[]
for i in range (1,n+1):
    if i%3 == 0 and i%5==0:
        answer.append("FizzBuzz")
    elif i%3 == 0 and i%5!=0:
        answer.append("Fizz")
    elif i%5==0 and i%3!=0:
        answer.append("Buzz")
    else:
        answer.append(str(i))
print(answer)