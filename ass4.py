#Question : 1
# create list from 1 to 10
numbers = list(range(1, 11))
print("Original list:", numbers)

#-------------------------------------------------------------------------------------------------------------
#Question : 2
# append operation (adds element at the end)
numbers.append(11)
print("After append(11):", numbers)

# insert operation (adds element at specific index)
numbers.insert(5, 99)  # inserts 99 at index 5
print("After insert(5, 99):", numbers)

#  ✅ Update using index
numbers[4] = 50   # update element at index 4 (5th element)
print("After updating index 4 with 50:", numbers)

# ✅ Delete using index
del numbers[2]    # deletes element at index 2 (3rd element)
print("After deleting element at index 2:", numbers)

# ✅ Delete using value
numbers.remove(10)  # deletes first occurrence of value 10
print("After removing value 10:", numbers)

# ✅ Sort the list in ascending order
numbers.sort()
print("Sorted list (ascending):", numbers)

# ✅ Sort the list in descending order
numbers.sort(reverse=True)
print("Sorted list (descending):", numbers)

# ✅ Reverse the list (just flips the order, no sorting)
numbers.reverse()
print("Reversed list:", numbers)

# ✅ Slice first 5 elements
first_five = numbers[:5]
print("First 5 elements:", first_five)

# ✅ Slice every second element
every_second = numbers[::2]
print("Every second element:", every_second)

# ✅Generate squares of even numbers from 1 to 10
squares_of_even = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares_of_even)

#-------------------------------------------------------------------------------------------------
#Question : 3
# ✅ Tuple with mixed types
mixed_tuple = (1, "python", 3.14)
print("Mixed tuple:", mixed_tuple)

# ✅ Single element tuple (note the comma!)
single_tuple = (5,)
print("Single element tuple:", single_tuple)

# ❌ Wrong way: without comma, it's just an integer
# not_a_tuple = (5)
# print("Without comma, it's:", type(not_a_tuple))

# ✅ Nested tuple (tuple inside a tuple)
nested_tuple = (1, (2, 3), ("a", "b"))
print("Nested tuple:", nested_tuple)

#-------------------------------------------------------------------------------------------------------------
#Question : 4
# create a tuple
my_tuple = (10, 20, 30, 20, 40, 50)

# ✅ Tuple unpacking
a, b, c, d, e, f = my_tuple
print("Unpacked values:", a, b, c, d, e, f)

# ✅ Access by index
print("Element at index 0:", my_tuple[0])   # first element
print("Element at index 3:", my_tuple[3])   # fourth element
print("Last element (using -1):", my_tuple[-1])

# ✅ count() method (how many times a value appears)
print("Count of 20:", my_tuple.count(20))

# ✅ index() method (first occurrence of a value)
print("Index of 30:", my_tuple.index(30))

#-------------------------------------------------------------------------------------------------------
#Question : 5
# create a list with duplicates
numbers_list = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]

# ✅ create a set from the list
#removes duplicates
numbers_set = set(numbers_list)

print("Original list:", numbers_list)
print("Set (duplicates removed):", numbers_set)

numbers_list = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]

# Copy of the list
numbers_list = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]
numbers_copy = list(numbers_list)
print("Original list:", numbers_list)
print("Copied list (duplicates kept):", numbers_copy)

#-------------------------------------------------------------------------------------------------------
#Question : 6
# ✅ add() method (adds an element)
numbers_set.add(10)
print("After add(6):", numbers_set)


# ✅ remove() method (removes an element)
numbers_set.remove(2)
print("After remove(2):", numbers_set)

# create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set1:", set1)
print("Set2:", set2)

# ✅ Union (all elements from both sets)
union_set = set1.union(set2)
print("Union:", union_set)

# ✅ Intersection (common elements in both sets)
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# ✅ Difference (elements in set1 but not in set2)
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

#----------------------------------------------------------------------------------------------------
#Question : 7
# set comprehension for squares divisible by 3
squares_div3 = {x**2 for x in range(1, 11) if x % 3 == 0}

print("Squares of numbers divisible by 3:", squares_div3)
