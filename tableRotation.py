#!/usr/bin/python
##################################################################################
# Author: Huaqin Xu (huaxu@ucdavis.edu)
# Supervisor: Alexander Kozik (akozik@atgc.org)
# Date: July. 12, 2006
# Description:
#
# This python script rotates rows and columns of the input table. 
#
# =================================================================================
# Prompt to input:
#	1.File name to be rotated:
#	2.Number of lines to skip from start (Default is 0)
# 	3.Delimiter to seperate columns/fields (Default is TAB)
#	4.Add AUTO_INCREMENT value at the first line? y/n (Default is n)
#
######################################################################################

import sys
import re
import array

# ---------------------------functions ------------------------------------------------
# -------------------------------------------------------------------------------------
def open_file(file_name, mode):
	try:
		the_file = open(file_name, mode)
	except(IOError), e:
		print "Unable to open the file", file_name, "Ending program.\n", e
		raw_input("\n\nPress the enter key to exit.")
		sys.exit(0)
	else:
		return the_file

# -------------------------------------------------------------------------------------
def writeToFile():
	global table
	global delimiter
	global rowcount
	global colcount

	for c in range(colcount):
		line = ""
		for r in range(rowcount):
			line = line + table[r][c]+ delimiter
		line=line.rstrip(delimiter)
		outf.write(line)
		if(c != colcount-1):
			outf.write('\n')
	

#----------------------------- main ------------------------------------------------------

#----- get input file name and construct output file name and open files -----
s = raw_input("# Enter the SOURCE file name: ")	
if s != "":
	ifile = s
else:
	print 'Empty input file name!'
	raw_input("\n\nPress the enter key to exit.")
	sys.exit(0)
	
ofile=ifile+'_rotate.out'

inf=open_file(ifile,'r')
outf=open_file(ofile,'w')

# ----- Prompt user to input -----
print '# Please provide the following information, ENTER to accept the DEFAULT setting!'
header = raw_input("... Number of lines to skip from start(Default - 0): ")
if header == "":
	header = 0
else:
	header = int(header)

delimiter = raw_input("... Columns/fields are seperated by(Default - TAB):")
if delimiter == "":
	delimiter = '\t'

auto=raw_input("... Add AUTO_INCREMENT value at the first line?(y/n)(Default - n):")
auto_field=[]
# ----- Read from input files ----- 
try:
	frows = inf.readlines()
except:
	print 'Failed to read from: ', ifile
	sys.exit(0)
 
linecount = len(frows)
if linecount==0:
	print 'Error: Failed to get row and/or col numbers at the first line!'
	sys.exit(0)

colcount = frows[header].count(delimiter)+1
table=[[]]* linecount

# ----- Loop through all the lines in the file -----
rowcount=0
emptyrow=0

print '# Processing ...'
for l in range(header, linecount):

	# check for empty lines and incorrect field numbers
	if frows[l] != '\n':
		if frows[l].count(delimiter)==colcount-1:
			frows[l]=frows[l].rstrip('\n')
			if auto == 'y':
				if rowcount != 0:
					auto_field=[str(rowcount)]
				else:
					auto_field=[';']
			table[rowcount]=auto_field+frows[l].split(delimiter)
			rowcount=rowcount+1
		else:
			print "Error: Line #%s is in wrong format.\n" %(l+1)
	else:
		emptyrow=emptyrow+1	

# ----- Finish Reading ----- 
print '... Skip %s empty rows' %(emptyrow)
print '... Read %s rows, %s columns' %(rowcount,colcount)

if auto == 'y': 
	colcount = colcount+1
writeToFile()

# ----- Print messages for user to find output ----- 
print '... Write %s rows, %s columns' %(colcount, rowcount)
print '... Please find output in file "%s"' %(ofile)

inf.close()
outf.close()

