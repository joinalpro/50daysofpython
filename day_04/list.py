# squares = []
# for num in range(2, 11):
#      square = num ** 2
#      squares.append(square)
# print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value ** 2 for value in range(1, 11)]
print(squares)

for n in digits:
    print(n * 2)