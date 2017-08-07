#numpy basics
import numpy as np
data = [[ 0.9526, -0.246 , -0.8856],
[ 0.5639, 0.2379, 0.9104]]
its = [1,2,4,5,5]
arr = np.array(data)
arr2 = np.array(its)

print(arr.ndim) #2
print(arr.shape) #(2,3)
print(arr.dtype) #float64
print(arr2.dtype)#int64


zeros = np.zeros(10)
print(zeros) #[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]

test = np.zeros((3, 6))
print(test)
# [[ 0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.]]

print(np.empty((2, 3, 2))) # 2 x 3 x 2
# [[[  6.94492811e-310   6.94492811e-310]
#   [  4.64399673e-310   4.64399673e-310]
#   [  4.64399673e-310   3.21142670e-322]]

#  [[  6.94492811e-310   6.94492811e-310]
#   [  6.94492876e-310   1.63041663e-322]
#   [  6.94492811e-310   6.94492811e-310]]]
#garbage vals 

print(np.arange(15))
#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

arr = np.array([[1, 2.0,3], [4, 5, 8]])
print(arr * 2)
# [[ 2  4  6]
#  [ 8 10 16]]



################################
#scalar vs arrrrrrrrrrrrrrrr
print(1 / arr)
# [[ 1.          0.5         0.33333333]
#  [ 0.25        0.2         0.125     ]]

#### Just noticed that np is playing loose with my commas!!!!!!!1111

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d[2]) #[7 8 9]
print(arr2d[2]) #[7 8 9]
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
l = np.random.randn(8, 4)
print(l)

arr = np.arange(15).reshape((3, 5))
print(arr)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

print(arr.T) #transpose
# [[ 0  5 10]
#  [ 1  6 11]
#  [ 2  7 12]
#  [ 3  8 13]
#  [ 4  9 14]]


# print(np.dot(arr.T, arr))
# [[125 140 155 170 185]
#  [140 158 176 194 212]
#  [155 176 197 218 239]
#  [170 194 218 242 266]
#  [185 212 239 266 293]]

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# res = [(a if c else b) for a, c, b in zip(xarr, cond, yarr)]


# print(res)
# [1.1000000000000001, 2.2000000000000002, 1.3, 1.3999999999999999, 2.5]

#np style

res = np.where(cond, xarr, yarr)
# print(res)

# [ 1.1  2.2  1.3  1.4  2.5]

arr = np.random.randn(4, 4)
print(arr)

# [[-2.34337633  0.71580762 -1.75229482 -0.60429395]
#  [-0.21339688  1.65560403 -2.36287915  0.37843413]
#  [-0.00287572  0.73619867 -2.33769568 -0.26058551]
#  [ 0.58544657  0.87944666  0.51955815 -0.68940446]]

res = np.where(arr>0, 2, -2)
# print(res)
# [[-2 -2  2  2]
#  [-2  2  2  2]
#  [-2  2 -2  2]
#  [-2 -2 -2  2]]

res = np.where(arr > 0, 2, arr) # set only positive values to 2
print(res)

cond1 = True
cond2 = False

res = np.where(cond1 & cond2, 0,
np.where(cond1, 1,
np.where(cond2, 2, 3)))



########################################
###  Mathematical and Statistical Methods
#########################################

#np.random.randn, mean, sum, cumsum, cumprod
# print(dir(arr))
# 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 
# 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 
# 'conj', 'conjugate', 'copy', 'ctypes', 'cumprod', 'cumsum', 
# 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 
# 'flags', 'flat', 'flatten', 'getfield', 'imag', 'item', 'itemset', 
# 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 
# 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 'real',
#  'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield',
#   'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 'strides',
#    'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring',
#     'trace', 'transpose', 'var', 'view'

####################################
##  Methods for Boolean Arrays
###################################

arr = np.random.randn(100)
# print(arr > 0).sum()


# Get a certai quantile
large_arr = randn(1000)
large_arr.sort()
large_arr[int(0.05 * len(large_arr))] # 5% quantile





















