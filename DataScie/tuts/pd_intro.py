from pandas import Series, DataFrame
import numpy as np

stock = Series([4, 3, 8, 9])

#stock
#Out[12]: 
#0    4
#1    3
#2    8
#3    9
#dtype: int64

# stock.values
# DataFrame, think csv
# pandas, think linear values
# numpy, think spreadsheets

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)

#Arithmetic methods with fill values
#indexwise arithmetics
df1 = DataFrame(np.arange(25).reshape(5,5), columns=list('abcde'), index=list('abcde'))
df2 = DataFrame(np.arange(25, 50).reshape(5,5), columns=list('abcde'), index=list('abcde'))

#df2
#Out[12]: 
#    0   1   2   3   4
#0   0   1   2   3   4
#1   5   6   7   8   9
#2  10  11  12  13  14
#3  15  16  17  18  19
#4  20  21  22  23  24

# =============================================================================
# df2.add(df1)
# Out[24]: 
#     0   1   2   3   4   a   b   c   d   e
# 0 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 1 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 2 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 3 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# 4 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# a NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# b NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# c NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# d NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# e NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
# =============================================================================
#reason is we got 0 common indexes

# =============================================================================
# df2.add(df1,fill_value=0)
# =============================================================================
# Out[31]: 
#     a   b   c   d   e
# a  25  27  29  31  33
# b  35  37  39  41  43
# c  45  47  49  51  53
# d  55  57  59  61  63
# e  65  67  69  71  73
# =============================================================================
# =============================================================================

#Operations between DataFrame and Series

arr = np.arange(12.).reshape((3, 4))
# =============================================================================
# array([[  0.,   1.,   2.,   3.],
#       [  4.,   5.,   6.,   7.],
#       [  8.,   9.,  10.,  11.]])
# =============================================================================

#n [34]: arr-arr[0]
#Out[34]: 
#array([[ 0.,  0.,  0.,  0.],
#       [ 4.,  4.,  4.,  4.],
#       [ 8.,  8.,  8.,  8.]])

#<<-- broadcatstig

frame = DataFrame(np.arange(12.).reshape((4,3)), columns=list('bde'),
index=['Fox', 'Cnn', 'Abc', 'Hbo'])
series=frame.ix[0]
series2 = Series(range(3), index=['b', 'e', 'f'])
#frame
#Out[37]: 
#       b     d     e
#Fox  0.0   1.0   2.0
#Cnn  3.0   4.0   5.0
#Abc  6.0   7.0   8.0
#Hbo  9.0  10.0  11.0
#
#frame - series
#Out[41]: 
#       b    d    e
#Fox  0.0  0.0  0.0
#Cnn  3.0  3.0  3.0
#Abc  6.0  6.0  6.0
#Hbo  9.0  9.0  9.0
#
#n [44]: frame + series2 
#Out[44]: 
#Fox  0.0 NaN   3.0 NaN
#Cnn  3.0 NaN   6.0 NaN
#Abc  6.0 NaN   9.0 NaN
#Hbo  9.0 NaN  12.0 NaN

# =============================================================================
# To broadcst over columns instead use df methods && specify axis
# =============================================================================

#series3 = frame['d']
#
#series3 
#Out[46]: 
#Fox     1.0
#Cnn     4.0
#Abc     7.0
#Hbo    10.0
#Name: d, dtype: float64
#
#frame.sub(series3, axis=0)
#Out[47]: 
#       b    d    e
#Fox -1.0  0.0  1.0
#Cnn -1.0  0.0  1.0
#Abc -1.0  0.0  1.0
#Hbo -1.0  0.0  1.0




# =============================================================================
# #Function application and mapping
# =============================================================================


frame = DataFrame(np.random.randn(9, 8), columns=list('abcdefgh'),
	index= ['New York', 'Indiana', 'Alabama', 'Georgia',
	'Washington', 'New Jersey', 'Texsas','Test', 'Lost'])

#frame
#Out[53]: 
#                   a         b         c         d         e         f  \
#New York   -0.661570 -0.895319 -1.402747 -1.648802 -0.632552  0.909815   
#Indiana    -0.453228 -1.697909 -0.765338  0.076564 -0.119203  0.018256   
#Alabama    -1.453918  0.448392  0.539369 -0.000963  0.444399 -1.099213   
#Georgia    -0.175848 -0.882784 -0.202698 -2.281018  1.394478  0.647207   
#Washington -0.255284 -0.632032 -0.069683 -1.595015 -0.147538  0.984192   
#New Jersey  0.117526  0.334670 -1.223019  1.196941  1.395554  0.607997   
#Texsas     -0.499998  1.974074  1.956290  0.186298  0.386323  1.620411   
#Test       -0.665570  0.863472  1.754348  0.552725  0.688808 -1.430362   
#Lost       -0.928069 -0.206633 -1.933997 -0.630691 -1.072648  0.140674   
#
#                   g         h  
#New York    1.179303 -1.019131  
#Indiana    -1.758359 -0.720638  
#Alabama     1.381439  0.606448  
#Georgia    -1.144267 -0.398720  
#Washington  0.024846 -0.704271  
#New Jersey -1.136606 -0.627800  
#Texsas     -0.733755  0.023039  
#Test        1.072744  1.014227  
#Lost       -0.760507  0.662007 
#rule is col x row and col maps to index
#np.abs(frame) --> obvious


#Apply a function to 1D arrays  to each column or row with 'apply' keyword
#think reduce

f = lambda x: x.max() - x.min()

def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)
#
#frame.apply(f)
#Out[61]: 
#a    2.985977
#b    3.085566
#c    2.187401
#d    3.863492
#e    3.479368
#f    3.815942
#g    3.701089
#h    4.230962
#dtype: float64

#for element wise, use applymap

format = lambda x: '%.2f' % x
frame.applymap(format)






obj = Series(range(4), index=['d', 'a', 'b', 'c'])
# obj.sort_index()
# Out[3]: 
# a    1
# b    2
# c    3
# d    0
# dtype: int64

# With a DataFrame, you can sort by index on either axis:

frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
columns=['d', 'a', 'b', 'c'])

# frame.sort_index()
# Out[5]: 
#        d  a  b  c
# one    4  5  6  7
# three  0  1  2  3

# frame.sort_index(axis=1)
# Out[8]: 
#        a  b  c  d
# three  1  2  3  0
# one    5  6MM  7  4


# Summarizing and Computing Descriptive Statistics

# Correlation and Covariance
import pandas_datareader.data as web
f = web.get_quote_google('AAPL')
c = web.get_data_yahoo('AAPL')

