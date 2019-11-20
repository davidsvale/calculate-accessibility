# calculate-accessibility
Python script to calculate accessibility (gravity-based and cumulative opportunities) from an origin-destination matrix.

## A bit of theory
   The literature contains several definitions of accessibility. The first comes from Hansen (1959, p. 73), which sees it as “the potential of opportunities for interaction”. Handy and Niemeier (1997, p. 1175) expand on the definition, noting that this potential is “determined by the spatial distribution of potential destinations, the ease of reaching each destination, and the magnitude, quality, and character of the activities found there”. Accessibility, therefore, reflects land use patterns that determine the spatial distribution of activities and the transport system; these, in turn, determine the ease of reaching a destination.
   
   We follow a place-based accessibility framework, in particular the designated gravity-based measures: opportunities are weighted as a function of their distance (physical or relative) from the origin following an impedance function. With the script is also possible to calculate cumulative opportunities measures, which are a special case of gravity-based measures. The latter adopt the same theoretical and methodological framework as the former, but assume a regular impedance function – specifically, opportunities located within a certain threshold are counted while others, beyond the threshold, are not. Although these measures are very sensitive to the threshold value, they are much easier to understand and explain, making them very important for planners and decision-makers.

## Requirements:
### Input files (`.csv`)
1) OD Matrix, with three columns: Origin, Destination, CostofTravel (column names are irrelevant, as long as they are in this order)
2) Data for opportunities found at destination (e.g. jobs at each location)

`<addr>`

### Impendance function
You need to define an impedance function to calculate accessibility.
It can be a rectangular function (to calculate cumulative opportunities measures) or an exponential function (in that case you need to set the value for beta)

### Output file
Results will be written to a csv file, which contains as many rows as origins in your OD Matrix. 
Please note that in the case of cumulative opportunities it might have a smaller number of rows, which means that the origin(s) missing have accessibility = 0. For instance, if you are calculating number of jobs accessible within 30 minutes, it simply means that that from that particular origin no job is accessible within 30 minutes.

# Files available to test the script

## Input files
OD_matrix.csv
DestinationData.csv

## Output files
AccResults.csv (by running the script you should get exactly the same file)


# Citation
If you have used this script in your work and you would like to cite it, you can use the following reference:
Vale, David (2019) Calculating gravity-based and cumulative opportunities from an OD matrix on python.  Retrieved from: https://github.com/davidsvale/calculate-accessibility

# References
Hansen, W.G., 1959. How accessibility shapes land use. Journal of the Am. Instute of Planners 25, 73–76.
Handy, S., Niemeier, D.A., 1997. Measuring accessibility: an exploration of issues and alternatives. Environment and Planning A 29, 1175–1194.
