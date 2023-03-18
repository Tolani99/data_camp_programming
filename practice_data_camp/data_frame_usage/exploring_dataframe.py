"""
To explore dataframe
We can perform the following
"""
# Import from basic modules
from basic_modules import df

# To print the first few lines of the dataframe
# print(df.head())

# To find the shape attribute of the dataframe
# print(df.shape)

# To find more information about the dataframe
print(df.info())

# To describe/compute some summary statistics
# Like mean, median etc we use describe method
# print(df.describe())

"""
DataFrame consists of three different components,
accessing using attributes
Value attribute - contains the data values in 2d Form
Columns attribute - contains column names
Index attribute - contains row names
"""
# To show the dat values
# print(df.values)

# To show the columns names
# print(df.columns)

# To show the rows numbers/names
# print(df.index)
