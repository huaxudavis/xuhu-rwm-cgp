#!/usr/bin/python
##################################################################################
# Author: Huaqin Xu (huaxu@ucdavis.edu)
# Supervisor: Alexander Kozik (akozik@atgc.org)
# Date: July. 13, 2006
# Description:
#
# This python script sorts a table by given the given header list. 
#
# =================================================================================
# Input Options:
#	1.Options: Sorted by row, col or both. (1, 2, 3 or 0 for exit)
#	2.File name of a table to be sorted.
#	3.File name of a list of sorted header.
#	4.If sorted by col, row header exists? y/n (Default is y)
#	5.Number of lines to ignore from start (Default is 0)
#	6.Line number of Header line located at (Default is 1)
#	7.Line number of real Data started (Default is 2)
# 	8.Delimiter to seperate columns/fields (Default is TAB)
#	9.Add AUTO_INCREMENT value at the first line? y/n (Default is n)
#
######################################################################################

import sys
import re
import array

# ---------------------------functions ------------------------------------------------
# ---------------- Open and read file functions ---------------------------------------
def open_file(prompt, mode):
	s = raw_input(prompt).strip()	
	if s != "":
		file_name = s
	else:
		print 'Empty input file name!'
		raw_input("\nPress the enter key to exit.")
		sys.exit(0)

	try:
		the_file = open(file_name, mode)
	except(IOError), e:
		print "Unable to open the file", file_name, "Ending program.\n", e
		raw_input("\nPress the enter key to exit.")
		sys.exit(0)
	else:
		return the_file

def read_file(afile):
	try:
		flines = afile.readlines()
	except:
		print 'Failed to read from: ', afile
		sys.exit(0)
	else:
		return flines

# ---------- check for empty lines and incorrect field numbers ---------------------------
def check_format(aline, colcount):
	global emptyrow
	global delimiter

	if aline == '\n':
		emptyrow=emptyrow+1
		return False
	else:
		if aline.count(delimiter)!=colcount-1:	
			print "Error: #%s\n is in wrong format.\n" %(aline)
			return False
		else:
			return True

# ---------------------------- Sort table function -------------------------------------
def writeToFile():
	global outf
	global autoheader
	global headerTable
	global dataTable
	global delimiter
	global rowkey
	global colcount

	rowcount=len(headerTable)+len(dataTable)
	if rowheaderExist == 'y' and opt!= '1':
		colcount=colcount+1

	if autoheader == 'y':
		outf.write(delimiter.join([str(k) for k in range(colcount)]) + '\n')
		rowcount=rowcount+1

	for l in headerTable:
		outf.write(delimiter.join(l)+'\n')

	for k in rowkey:
		outf.write(delimiter.join(dataTable[k])+'\n')

	# ----- Print messages for user to find output ----- 
	print '... Write %s rows, %s columns' %(rowcount, colcount)

#---------------------------------------------------
def sortByRow():
	global inputflines
	global rowflines
	global headerTable
	global dataTable
	global omitAt
	global dataAt
	global rowkey
	global colcount
	
	for l in range(omitAt, len(inputflines)):
		if check_format(inputflines[l], colcount):
			aline=inputflines[l].rstrip().split(delimiter)
			if l < dataAt:
				headerTable.append(aline)
			else:
				dataTable[aline[0]]=aline		

	rowkey=[k.strip() for k in rowflines if k.strip() in dataTable.keys()]


#---------------------------------------------------
def sortByCol():
	global inputflines
	global colflines
	global headerTable
	global dataTable
	global omitAt
	global dataAt
	global colheader
	global rowheaderExist
	global colcount
	global rowkey

	colkey=[k.strip() for k in colflines if k.strip() in colheader]
	for l in range(omitAt, len(inputflines)):
		if check_format(inputflines[l], colcount):
			aline=inputflines[l].rstrip().split(delimiter)
			linedict=dict(zip(colheader,aline))
			linesorted=[linedict[k] for k in colkey]
			if rowheaderExist == 'y':
				linesorted = [aline[0]]+linesorted
			
			if l<dataAt:
				headerTable.append(linesorted)
			else:
				dataTable[l]=linesorted
				rowkey.append(l)

	colcount=len(colkey)

#---------------------------------------------------
def sortByBoth():
	global inputflines
	global colflines
	global rowflines
	global headerTable
	global dataTable
	global omitAt
	global dataAt
	global colheader
	global rowkey
	global colcount

	colkey=[k.strip() for k in colflines if k.strip() in colheader]
	for l in range(omitAt, len(inputflines)):		
		if check_format(inputflines[l], colcount):
			aline=inputflines[l].rstrip().split(delimiter)
			linedict=dict(zip(colheader,aline))
			linesorted=[linedict[k] for k in colkey]
			linesorted = [aline[0]]+linesorted
			
			if l < dataAt:
				headerTable.append(linesorted)
			else:
				dataTable[aline[0]]= linesorted
	
	rowkey=[k.strip() for k in rowflines if k.strip() in dataTable.keys()]
	colcount=len(colkey)	
	

#----------------------------- main ------------------------------------------------------

# ----- get options and file names and open files -----
print '# Select the options: (Default - 0)'
print '0. Exit'
print '1. Sort by row '
print '2. Sort by column '
print '3. Sort by both row and column'
opt = raw_input('Your choice is: ').strip()

if opt != '1' and opt != '2' and opt != '3':
	print '... Exit tableSort program now!'
	sys.exit(0)
else:
	tablef=open_file("# Enter file name to be sorted: ",'r')
	inputflines = read_file(tablef)

	if opt == '1' or opt == '3':
		rowf=open_file("# Enter file name of the sorted row header: ", 'r')
		rowflines = read_file(rowf)

	if opt == '2' or opt == '3':
		colf=open_file("# Enter file name of the sorted column header: ", 'r')
		colflines = read_file(colf)
	
	outf=open_file("# Enter file name of the output: ",'w')

# ----- Prompt user to input -----
print '# Please provide the following information, ENTER to accept the DEFAULT setting!'
#---------------------------------------------------
rowheaderExist = 'y'
if opt=='2':
	rowheaderExist = raw_input("... Row header exists(y/n)(Default - y):").strip()
	if rowheaderExist == "":
		rowheaderExist = 'y'

#---------------------------------------------------
omitAt = raw_input("... Number of lines to skip from start(Default - 0): ").strip()
if omitAt == "":
	omitAt = 0
else:
	omitAt = int(omitAt)

#---------------------------------------------------
dataAt = raw_input("... Real Data starts from line #(Default - 2): ").strip()
if dataAt == "":
	dataAt = 1
else:
	dataAt = int(dataAt)-1

if omitAt > dataAt:
	print 'Error: Wrong location of omit line or data line!'
	sys.exit(0)

#---------------------------------------------------
colheaderAt = 0
if opt == '2' or opt == '3':
	colheaderAt = raw_input("... Column headerline locates at line #(Default - 1): ").strip()
	if colheaderAt == "":
		colheaderAt = 0
	else:
		colheaderAt = int(colheaderAt)-1

	if colheaderAt < omitAt or colheaderAt >= dataAt:
		print 'Error: Wrong location of row headerline!'
		sys.exit(0)

delimiter = raw_input("... Columns/fields are seperated by(Default - TAB):").strip()
if delimiter == "":
	delimiter = '\t'

autoheader=raw_input("... Add AUTO_INCREMENT value at the first line?(y/n)(Default - n):").strip()

# ----- Loop through all the lines in the file -----
if len(inputflines)==0:
	print 'Error: Failed to get row and/or col numbers at the first line!'
	sys.exit(0)
else:
	headerTable=[]
	dataTable={}
	rowkey=[]
	rowcount=len(inputflines)
	colheader=inputflines[colheaderAt].strip().split(delimiter)
	colcount=len(colheader)

	emptyrow=0

	# ----- Start Reading ----- 	
	print '# Processing ...'
	print '... Read %s rows, %s columns' %(rowcount,colcount)

	if opt=='1':
		sortByRow()

	if opt=='2':
		sortByCol()

	if opt=='3':
		sortByBoth()

	writeToFile()

	print '... Skip %s empty rows' %(emptyrow)



tablef.close()
outf.close()
if opt=='1' or opt=='3':
	rowf.close()
if opt=='2' or opt=='3':
	colf.close()

