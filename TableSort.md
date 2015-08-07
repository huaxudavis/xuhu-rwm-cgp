# Script to sort a table
## Summary ##

This python script sorts a table by the given header list with the following options.

### Options ###

  * Sorted by row, col or both. (1,2,3 or 0 for exit)
  * File name of a table to be sorted.
  * File name of a list of sorted header.
  * If sorted by col, row header exists? y/n (Default is y)
  * Number of lines to ignore from start (Default is 0)
  * Line number of Header line located at (Default is 1)
  * Line number of real Data started (Default is 2)
  * Delimiter to seperate columns/fields (Default is TAB)
  * Add AUTO\_INCREMENT value at the first line? y/n (Default is n)


### Example Command ###
```
$ python tableRotation.py
# Select the options: (Default - 0)
0. Exit
1. Sort by row
2. Sort by column
3. Sort by both row and column
Your choice is: 3
# Enter file name to be sorted: Ath_SFP_Scores_0846_Rand.lg1_Shfl.map.loc
# Enter file name of the sorted row header: example_sorted_list_2_M.txt
# Enter file name of the sorted column header: example_sorted_list_1_R.txt
# Enter file name of the output: Ath_SFP_Scores_0846_Sort.out
# Please provide the following information, ENTER to accept the DEFAULT setting!
... Number of lines to skip from start(Default - 0): 1
... Real Data starts from line #(Default - 2): 4
... Column Headerline locates at line #(Default - 1): 3
... Columns/fields are seperated by(Default - TAB):
... Add AUTO_INCREMENT value at the first line?(y/n)(Default - n):y
# Processing ...
... Read 212 rows, 149 columns
... Write 212 rows, 149 columns
... Skip 0 empty rows
```

### Input file ###
  * [Ath\_SFP\_Scores\_0846\_Rand.lg1\_Shfl.map.loc](http://xuhu-rwm-cgp.googlecode.com/svn/trunk/data/Ath_SFP_Scores_0846_RIL.lg1.map.loc)
  * [example\_sorted\_list\_2\_M.txt](http://xuhu-rwm-cgp.googlecode.com/svn/trunk/data/example_sorted_list_2_M.txt)
  * [example\_sorted\_list\_1\_R.txt](http://xuhu-rwm-cgp.googlecode.com/svn/trunk/data/example_sorted_list_1_R.txt)

### Output file ###
  * [Ath\_SFP\_Scores\_0846\_Sort.out](http://xuhu-rwm-cgp.googlecode.com/svn/trunk/data/Ath_SFP_Scores_0846_Sort.out)