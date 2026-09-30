"""
Problem:
RichestCustomerWealth

Difficulty:
Easy

Approach:
Array, matrix

Time Complexity:
O(n)

Space Complexity:
O(n)
"""
rich = 0
matrix = []
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    row = []
   
    for j in range(cols):
    
        element = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)
        
print("Nested List:", matrix)

rich = 0
for row in matrix:
    wealth = 0
    for money in row:
        wealth += money 

    rich = max(rich, wealth)

print(f"the richest person has wealth: {rich}")
