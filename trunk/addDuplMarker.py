#!/usr/bin/python
##################################################################################
# Author: Huaqin Xu (huaxu@ucdavis.edu)
# Supervisor: Alexander Kozik (akozik@atgc.org)
# Date: June. 19 2006
# Description:
#
# This python script inserts duplicate markers into map file. 
#
# =================================================================================
# Input file:
# 1. Map file:
#	Map file contains at least three fields: Prefix, MarkerID and Score, which are delimited by tab. 
#
# -- Examples	
#   [Prefix]   [MarkerID]  [Score]   	 
#     |           |           |
#   	LG		LE0295     44			
#   	LG		LE0310     1050			
#   
# 2. Marker file:
#	Marker file contains at least three fields: MarkerID, MasterID and Status, which are delimited by tab. 
#
# -- Examples	
#   [MarkerID]   [MasterID]  [Status]   	 
#     |           |           |
#   	LE0295	LE0295	-=+unique+=-
#	LE0310	LE0310	-=+master+=-
#	LE0329	LE0310	 -- dupl -- 	
#
# ---------------------------------------------------------------------------------
# Output file format:
# 	Ouput file contains five fields: Prefix, MarkerID, Score, MasterID and Status, which are delimited by tab. 
#
#    [Prefix]   [MarkerID]	[Score]   [MasterID]  	[Status]   
#     |           |           |		|			|
#   	LG		LE0295     44		LE0295	-=+unique+=-	
#   	LG		LE0310     1050		LE0310	-=+master+=-
#	LG		LE0310     1050		LE0310	 -- dupl -- 	
#	
######################################################################################
import sys
import re

# ---------------------------functions ------------------------------------------------
# -------------------------------------------------------------------------------------

def open_file(file_name, mode):
	try:
		the_file = open(file_name, mode)
	except(IOError), e:
		print "Unable to open the file", file_name, "Ending program.\n", e
		raw_input("\n\nPress the enter key to exit.")
		sys.exit()
	else:
		return the_file


# -------------------------------------------------------------------------------------

def getMark():
	global flines
	global mark
	global skipMark
	
	for i in flines:
		aline = i.rstrip().split('\t')
		if len(aline)>2:
			mark[aline[0]]=(aline[1], aline[2])
		else:
			skipMark +=1
	
def getMap():
	global mlines
	global map
	global key
	global skipMap
	
	for j in mlines:
		aline = j.rstrip().split('\t')
		if len(aline)>2:
			map[aline[1]]=(aline[0], aline[1], aline[2])
			key.append(aline[1])
		else:
			skipMap +=1

def getResult():
	global outf
	global mark
	global map
	global result
	global key
	global outcount
	
	for l in key:
		outf.write('\t'.join(map[l])+'\t'+'\t'.join(mark[l])+'\n')
		outcount+=1
		if mark[l][1] != '-=+unique+=-':
			slave=[i for i in mark.keys() if mark[i][0] == l and mark[i][1] == ' -- dupl -- ']
			for j in slave:
				outf.write('\t'.join((map[mark[l][0]][0], j , map[mark[l][0]][2]))+'\t'+'\t'.join(mark[j])+'\n')
				outcount+=1
	
		
#----------------------------- main ------------------------------------------------------
# ----- get input files' name and construct output file name and open files -----

s = raw_input("Enter the Marker file name: ")	
if s != "":
	ifile = s
else:
	print 'Empty input file name!'
	raw_input("\n\nPress the enter key to exit.")
	sys.exit(0)

s = raw_input("Enter the Map file name: ")	
if s != "":
	mfile = s
else:
	print 'Empty input file name!'
	raw_input("\n\nPress the enter key to exit.")
	sys.exit(0)

ofile=mfile+'_dupl.out'

inf=open_file(ifile,'r')
mapf=open_file(mfile, 'r')
outf=open_file(ofile,'w')

try:
	flines = inf.readlines()
except:
	print 'Failed to read from: ', ifile
	sys.exit(1) 
markcount = len(flines)
try:
	mlines = mapf.readlines()
except:
	print 'Failed to read from: ', mfile
	sys.exit(1) 
mapcount = len(mlines)

skipMap=0
skipMark=0
outcount=0

map={}
mark={}
result={}
key=[]

getMark()
getMap()
getResult()

print 'Processing ... ...'
print '...... Read Map %s lines, skip %s lines' %(mapcount, skipMap)
print '...... Read Marker %s lines, skip %s lines' %(markcount, skipMark)
print '...... Write Output %s lines' %(outcount)
print 'Please find output in file %s' %(ofile) 

inf.close()
mapf.close()
outf.close()