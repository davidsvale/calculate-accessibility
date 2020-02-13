# calculate-accessibility (version 2.0, Jan 2020)
Python script to calculate accessibility (gravity-based, cumulative opportunities, gaussian and cumulative-gaussian) from an origin-destination matrix.

## A bit of theory
   The literature contains several definitions of accessibility. The first comes from Hansen (1959, p. 73), which sees it as “the potential of opportunities for interaction”. Handy and Niemeier (1997, p. 1175) expand on the definition, noting that this potential is “determined by the spatial distribution of potential destinations, the ease of reaching each destination, and the magnitude, quality, and character of the activities found there”. Accessibility, therefore, reflects land use patterns that determine the spatial distribution of activities and the transport system; these, in turn, determine the ease of reaching a destination.
   
   We follow a place-based accessibility framework, in particular the designated gravity-based measures: opportunities are weighted as a function of their distance (physical or relative) from the origin following an impedance function. With the script is also possible to calculate cumulative opportunities measures, which are a special case of gravity-based measures. The latter adopt the same theoretical and methodological framework as the former, but assume a regular impedance function – specifically, opportunities located within a certain threshold are counted while others, beyond the threshold, are not. Although these measures are very sensitive to the threshold value, they are much easier to understand and explain, making them very important for planners and decision-makers.

### Formula used
In this script we calculate accessibility of place *i* as:

<a href="https://www.codecogs.com/eqnedit.php?latex=A{i}&space;=&space;\sum_{j=1}^n&space;O_jf(C_i_j)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A{i}&space;=&space;\sum_{j=1}^n&space;O_jf(C_i_j)" title="A{i} = \sum_{j=1}^n O_jf(C_i_j)" /></a>

For a deeper understanding of methodologies to calculate accessibility, we refer you to:

Vale, D. S., Saraiva, M., & Pereira, M. (2015). Active accessibility: A review of operational measures of walking and cycling accessibility. Journal of Transport and Land Use, 9(1). https://doi.org/10.5198/jtlu.2015.593 (Open Access)

For a deeper understanding of the impedance functions used, and its impact on pedestrian accessibility:

Vale, D. S., & Pereira, M. (2017). The influence of the impedance function on gravity-based pedestrian accessibility measures: A comparative analysis. Environment and Planning B: Urban Analytics and City Science, 44(4), 740–763. https://doi.org/https://doi.org/10.1177/0265813516641685


## Requirements:
### Input files
1) OD Matrix, with three columns: Origin, Destination, CostofTravel (column names are irrelevant, as long as they are in this order)
2) Data for opportunities found at destination (e.g. jobs at each location)

### Impendance function
With this script, we calculate:
1) an exponential function
2) a rectangular function
3) a Gaussian function
4) a cumulative-Gaussian function

You need to set the paramteres of these funcions, namely:
1) the value for the beta for the exponential function (default value is -0.0384)
2) the value for delta for the rectangular function (the threshold, default value = 30)
3) the value for v for the Gaussian function (default value = 324.60614)
4) the value for a and v for the cumulative-Gaussian function (default values a= 30, v = 324.60614)

We are providing two scripts, exactly the same, but one has these parameters set for pedestian accessibility calculations, assuming that the OD matrix has been calculated as walking distance between origins and destinations.

You can alter the parameters in both files (`AccFromODMatrix_v2.py` and `AccFromODMatrix_Walk.py`), but we recomend you to use `AccFromODMatrix_Walk.py` if you are calculating pedestrian accessibility.

### Output file
Results will be written to a csv file, which contains as many rows as the number of origins in your OD Matrix. 


# Files available to test the script
Please copy all files to the same directory and run the script `AccFromODMatrix_v2.py`

## Input files
`OD_Matrix.csv` : file with OD matrix (1054 Origins x 1054 Destinations)
Please note this file is zipped, so you need to unzippit first.
(If you are using `AccFromODMatrix_Walk.py`, you should use `OD_Matrix_Walk.csv`)

`DestinationData.csv`: file with data for opportunities found at destinations (in this example residents at each destination)

## Output files
`AccResults.csv` : file with the results for the 1054 origins with four columns: 'Acc_exponential', 'Acc_cumulative', 'Acc_Gaussian' and 'Acc_CumGaussian' 
By running the script you should get exactly the same file.


# Citation
If you have used this script in your work and you would like to cite it, you can use the following reference:
Vale, David (2020) Calculate accessibility from an OD matrix on python (version 2.0).  Retrieved from: https://github.com/davidsvale/calculate-accessibility

# References
Hansen, W.G., 1959. How accessibility shapes land use. Journal of the Am. Instute of Planners 25, 73–76.
Handy, S., Niemeier, D.A., 1997. Measuring accessibility: an exploration of issues and alternatives. Environment and Planning A 29, 1175–1194.
