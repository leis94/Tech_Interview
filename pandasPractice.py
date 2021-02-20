
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

import os
import pandas as pd


def readSingleColumn(df, column_name):
   """ 
   This function validates if the column name exists in the data frame and returns a single column given from the original df. Otherwise, it returns the message: This column does not exist.
   """
   list_of_columns = list(df)
   if column_name in list_of_columns:
      return (df[column_name])
   else:
      return('This column does not exists')


def returnListFromColumn(series):
   """ 
   This function returns a list of python from a series previously gaven from a single column from a df.
   I chose to return a list since it is a Python structured data type for querying data. Arrys are most used to perform mathematical operations.
   """
   lista = series.tolist()
   return lista


def searchPlayersOlderbyAge(df, age):
   """ 
   This function returns a data subbox filter given a value in the Age column, in this case, it filters by the condition Age is greater than the given number.
   """   
   sub_df = df[df['Age'] > age]
   return sub_df


def merge2Dataframes(df1, df2):
   """
   This function merge two dataframes with the inner operation.
   """
   df_merged = df1.merge(df2, how='inner', on=list(df1))
   return df_merged


def exportDataframetoExcel():
   """
   This function exports from a dataframe to an excel document, previously validating if the document exists where you delete it to recreate it.
   """
   if os.path.exists("nba_merged.xlsx"):
      os.remove("nba_merged.xlsx")
      df_merged.to_excel('nba_merged.xlsx')
   else:
      df_merged.to_excel('nba_merged.xlsx')


if __name__ == '__main__':

   # 1
   df_read = pd.read_excel('nba.xlsx')
   print(df_read)

   # Change Column name due Height has datetime type should be a Date column name insted of Heigth
   df_read.rename(columns={'Height':'Date'}, inplace=True)
   print(df_read)

   # 2
   read_column = readSingleColumn(df_read, 'Name')
   print(read_column)

   # 3
   returnList = returnListFromColumn(read_column)
   print(returnList)
   print(type(returnList))

   # 4
   olderPlayers = searchPlayersOlderbyAge(df_read, 29)
   print(olderPlayers)

   # 5
   # Read the nba2.xlsx file as read the first one and Change Column name due Height has datetime type should be a Date column name insted of Heigth
   df_read_2 = pd.read_excel('nba2.xlsx')
   df_read_2.rename(columns={'Height':'Date'}, inplace=True)


   dict_dfs={'df1': df_read,
      'df2': df_read_2
   }

   df_merged = merge2Dataframes(**dict_dfs)
   print(df_merged)

   # 6
   exportDataframetoExcel()
