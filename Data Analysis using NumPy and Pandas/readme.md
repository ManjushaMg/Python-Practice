Data Analysis using NumPy and Pandas


Steps followed

1.created 1D and 2D arrays for the given value: Found out its shape(shape()),data type(dtype()),no.of elements etc, and done some arithmetic operations (min,max etc)


2.Indexing and slicing: Found out values that meet specific condition by performing slicing and indexing

3.Pandas Series:

a) Creating a Pandas Series

Created a Pandas Series using the given marks, with custom index labels representing student ranks (Rank1, Rank2, Rank3, etc.).

b)indexing and slicing: displayed first rank student's mark, retrieved marks of required students(loc,iloc), filtered ranks where marks>90 (Boolean indexing)

c)modification: changing marks, removing entry and performed calculation to find out cgpa

4.Pandas dataframe

a)created the frame from given list of values


b)data analysis: used info(),shape(),column(),head(),tail() to find out basic details, displayed only desired columns, slicing and indexing for better analysis(loc,groupBy,& operator, unique(),valuecounts(), and performed arithmetic operations)

c)modified dataframe: created another column 'Discount',removed it(drop),changed values of existing entries

 Through this assignment I learned  how to use NumPy and Pandas library and its features for data exploration and analysis
 also some learnings gained from errors:
  1.Pandas Series Deletion: Once an entry is deleted, it cannot be deleted again unless it is added back to the Series

2.Pandas operations like drop() return a new DataFrame by default.To retain the changes,assign the result back to the original variable 
