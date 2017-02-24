import random

# R-1.1
# Write a short Python function, is_multiple(n,m) that takes two integer values and returns True if n is a multiple of m, that is,
# n = mi for some integer i, and False otherwise.

def is_multiple(n,m):
	return True if m % n == 0 else False


# testing is_multiple
print("Testing the is_multiple function")
print(is_multiple(3,15))
print(is_multiple(4,15))

# R-1.2
# Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise.
# However your function cannot use the multiplication, modulo, or division operators

def is_even(k):
	return False if k & 1 else True

#testing is_even
print("\nTesting the is_even function")
print(is_even(2))
print(is_even(3))

# R-1.3
# Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two.
# Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
	largest = data[0]
	smallest = data[0]
	for item in data:
		if item > largest:
			largest = item
		elif item < smallest:
			smallest = item
	return smallest,largest

# testing minmax
print("\nTesting the minmax function")
alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]
print(minmax(alpha))

# R-1.4
# Write a short Python function that takes a positive integer n and returns the sum of the squares
#  of all the positive integers smaller than n.

def sumofsquares(n):
	n -= 1
	total = 0
	while n > 0:
		total += n * n
		n -= 1
	return total

# testing sumofsqaures
print("\nTesting sumofsquares function")
print(sumofsquares(4))


# R-1.5
# give a single command that computes the sum from exercise r-1.4, relying on python's comprehension syntax and built in sum function

def sumofsquares2(n):
	return sum([k * k for k in range(0,n)])

#testing sumofsquares2
print("\nTesting sumofsquares2 function")
print(sumofsquares2(4))

# R-1.6
#Write a short Python function that takes a positive integer n and returns the sum of the squares
# of all the odd positive integers smaller than n.

def odd_sum_of_squares(n):
	n -= 1
	total = 0
	while n > 0:
		if n & 1:
			total += n*n
		n -= 1
	return total

print("\nTesting odd_sum_of_squares function")
print(odd_sum_of_squares(4))


