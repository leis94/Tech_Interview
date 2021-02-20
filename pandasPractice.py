
"""
Second Part: Create your code.

In this module you should implement a code that reads the file
nba.xlsx (taken from https://www.geeksforgeeks.org/python-pandas-dataframe/)
and import it as a pandas dataframe and process it.

There should be functions or methods that:

0) Read and import excel file into pandas dataframe (df)
1) Prints the df
2) Return a df with a single given column from the original df
3) Return a list or array (explain choise) from a given column
4) Return a sub-dataframe filtered by a column value
5) Return the merge of two dataframes (you can use the nba2.xlsx)
   with an inner join.
6) Output a given dataframe to an excel file.


Third Part: Challenge yourself
            Implement a simple API in Django with a storage
            in Postgresql that uses the methods for processing
            developed with pandas.
"""

import pandas as pd


def readSingleColumn(df, column_name):
    """ This function validates if a column name exists in dataframe and returns a single column given from the original df
        Otherwise returns the message: This columns does not exists
    """
   list_of_columns = list(df)
   if column_name in list_of_columns:
      return (df[column_name])
   else:
      return('This columns does not exists')


def returnListFromSeries(series):
   """ This function returns a list of python from a series previsoly gaven from a single column from a df.
      I choosed return a list due is a data structured from python to consult data. Arryas are used to calculate
   """
   lista = series.tolist()
   return lista


if __name__ == '__main__':

    # 1
    df_read = pd.read_excel('nba.xlsx')
    print(df_read)

    # 2
    read_column = readSingleColumn(df_read, 'Name')
    print(read_column)

    # 3
    returnList = returnListFromSeries(read_column)
    print(returnList)
    print(type(returnList))
