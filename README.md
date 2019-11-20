# calculate-accessibility
Python script to calculate accessibility (gravity and cumulative opportunities) from OD matrix.

## A bit of theory

## Requirements:
### Input files
1) OD Matrix (csv file), with three columns: Origin, Destination, CostofTravel (column names are irrelevant, as long as they are in this order)
2) Data for opportunities found at destination (e.g. jobs at each location)

### Impendance function
You need to define an impedance function to calculate accessibility.
It can be a rectangular function (to calculate cumulative opportunities measures) or an exponential function (in that case you need to set the value for beta)

### Output file
Results will be written to a csv file, which contains as many rows as origins in your OD Matrix. 
Please note that in the case of cumulative opportunities it might have a smaller number of rows, which means that the origin(s) missing have accessibility = 0. For instance, if you are calculating number of jobs accessible within 30 minutes, it simply means that that from that particular origin no job is accessible within 30 minutes.
