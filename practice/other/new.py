# phone =input("phone:")
# digits_mapping = {
#   "1":"one",
#   "2":"two",
#   "3":"three",
#   "4":"four"
# }
# output = ""
# for ch in phone:
#   output += digits_mapping.get(ch, "!") + " "
# print(output)
 

# emoji converter
# massage = input('>')
# words = massage.split(' ')
# emojis = {
#  ":)": "😊",
#   ":(": "😢",
# }
# print(words)

# try:
#   age = int(input("age: "))
#   income = 20000
#   risk = income / age
#   print(risk)
# except ZeroDivisionError:
#      print("age cannot be 0")
# except ValueError:
#   # handle the ValueError exception
#   print("invalid value")


# for num in range(1,10):
#   if num % 2 == 0:
#     print(num)
# else:
#   print("here are the 4 even numbers")

# letters = [1,2,3,4,5,6,66]
# for letter in enumerate(letters) :
#   print(letter[0],letter[1])

# instead #

# letters = [1,2,3,4,5,6,66]
# for index, letters in enumerate(letters):
#   print(index,letters)

# # add
# letters = ["a","b","c"]
# letters.append("d")
# letters.insert(2,"v")

# # remove
# letters.pop(2)
# letters.remove("a")
# del letters[1]
# letters.clear( )
# print(letters)

# # finding items in a list
# letters = ["a","b","c"]
# lets = letters.index("b")
# print(lets)

# # sorting item in a list 
# numbers = [1,3,4,5,23,45,0]
# # numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# # print(numbers)

# items = [
#   ("product1", 10),
#   ("product2", 9),
#   ("product3",12)
# ]
# def sort_item(item):
#   return item[1]

# items.sort( 
#   key = sort_item )
# print(items)

# nums = [1,2,34,6,5]
# print(sorted(nums))
# print(nums)

# items = [
#   ("product1", 10),
#   ("product1", 5),
#   ("product1", 4),
#   ("product1", 12)
# ]

# def sort_item(item):
#   return item[1]


# items.sort(key = sort_item)
# print(items)

# modifying string

numbers = input("Enter the numbers: ").split()
print(numbers)