# List - Shopping List
# milk, bread, butter, poha
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit

shopping = ["milk", "bread", "butter", "poha"]
print(shopping)
print(len(shopping))
print(shopping[0])
print(shopping[-1])

shopping.append("curd") # Add item in the end
print(shopping)

shopping.insert(3, "jam") # Add item in the middle
print(shopping)

shopping.extend(["chips", "salt"]) # Add multiple items in the end
print(shopping)

shopping.remove("bread") # Remove item
print(shopping.pop())
print(shopping.index("butter"))
shopping.reverse()
shopping.sort()
print(shopping)
shopping[0] ="Uday"
print(shopping)
print(type(shopping))


my_list = [1, 2, 3, 4, True, 3.14, "Pramod"]
print(type(my_list))  # <class 'list'>
