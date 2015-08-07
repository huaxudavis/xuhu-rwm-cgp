# Script to insert redundant markers into map

## Summary ##

This script is designed to insert the redudant markers into map file

### Sample Command ###
```
$ python addDuplMarker.py
Enter the Map file name: RIL_2006_11_15.JM_ABH.map
Enter the Marker file name: ril_data_2006_11_15XX.90RILs.recbit.z_marker_sum
Processing ... ...
...... Read Map 1391 lines, skip 0 lines
...... Read Marker 1704 lines, skip 0 lines
...... Write Output 1444 lines
Please find output in file "RIL_2006_11_15.JM_ABH.map_dupl.out"

```

### Input file ###

Map file:
  * contains at least three fields: Prefix, MarkerID and Score, which are delimited by tab.
  * example file: [RIL\_2006\_11\_15.JM\_ABH.map](http://xuhu-rwm-cgp.googlecode.com/svn/trunk/data/RIL_2006_11_15.JM_ABH.map)

Marker file:
  * contains at least three fields: MarkerID, MasterID and Status, which are delimited by tab.
  * example file: [ril\_data\_2006\_11\_15XX.90RILs.recbit.z\_marker\_sum](http://xuhu-rwm-cgp.googlecode.com/svn/trunk/data/ril_data_2006_11_15XX.90RILs.recbit.z_marker_sum)

### Output file ###
  * contains five fields: Prefix, MarkerID, Score, MasterID and Status, which are delimited by tab.
  * example file: [RIL\_2006\_11\_15.JM\_ABH.map\_dupl.out](http://xuhu-rwm-cgp.googlecode.com/svn/trunk/data/RIL_2006_11_15.JM_ABH.map_dupl.out)