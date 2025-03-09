# for loop
# 3 types of statement i, sequencial ii, conditional iii, repeatable statement

# Iterables: list , tuple, set, dictionary, strings

nums = [23, 25, 33, 26, 39]
# here item like a variable
# tuple (2, 3, 4, 5)
# set {3, 4, 5, 6}
# dictionary {"key": "value", "name": "joinal"}
for item in nums:
    print("Item ", item ** 10)
    
li = ["ko", "Ko", "choclate"]
for i in li:
    print("Item: ", i)
    
for index in range(len(li)):
    print(list[index])
    
lang = ['R', 'python', 'Go']
for i in lang:
    print(i)