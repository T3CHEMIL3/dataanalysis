import numpy as np

#create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)

#create a 2D array
arr_2 = np.array([[1,2,3], [4,5,6]])
print("2D Array:\n", arr_2)

#Array of zeros
zeros = np.zeros((3, 3))
print("Array of zeros:\n", zeros)

#Array of random numbers
random_nums = np.random.rand(3,3)
print("Random Array:\n", random_nums)

#Element-wise operations
arr = np.array([10, 20, 30])
print("Add 5 to element:", arr + 5)
print("Multiply each by 2:", arr * 2)
