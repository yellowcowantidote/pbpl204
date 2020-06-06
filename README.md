# Employment Centers in Southern California

This project examines regional employment centers in San Diego and Riverside metropolitan areas. It begins by identifying a set of centers in each metro, then we use segregation/spatial concentration statistics to characterize each center.

## Setup

1. Clone this repository
2. Run `conda env create -f environment.yml` to build the conda environment with necessary dependencies
   - run `conda activate pbpl204` each time you work on the project

## Running the Analysis:

The analysis is executed entirely through Jupyter notebooks stored in the `notebooks` folder.
The notebooks do the following and should be executed in this sequence:

1. `center_smoother_rv_revised.ipynb` and `center_smoother_sd_revised.ipynb`
   These notebooks identify the employment centers in the San Diego and Riverside metropolitan areas at the tract level. They write out the data to GeoJSON files that are placed in the data folder.

2. `SDCounty.ipynb` and `RIVCounty.ipynb`
   
   These notebooks utilize the GeoJSON files created in the last step to generate interactive visualizations displaying total employment of each center as well as the ability to create visualizations of each NAICS code with its corresponding Location Quotient from the `pf.graph_codes` function.

## Results:

After running all the notebooks, we're left with a set of polygons that define regional employment centers in both Riverside and San Diego. As previously stated, `RIVCounty.ipynb` and `SDCounty.ipynb` have interactive maps displaying these centers and the ability to display by NAICS code.

### San Diego

We find roughly 8 employment centers in San Diego. It should be noted that our methods actually identify 13 separate employment centers in San Diego, but we can assume that some of them are apart of the same center due to their proximity. The centers can be identified as:
1. Downtown San Diego - including Hillcrest, Mission Hills and Mission Valley
2. Kearny Mesa
3. UCSD and sorrounding hospitals/retail
4. The core of Chula Vista
5. Much of the City of La Mesa
6. Much of the City of El Cajon
7. Much of the City of Poway
8. The western portion of San Marcos

Taking a closer look at these centers, it seems that many of them contain shopping malls or other high profile destinations for retail. Many of them also contain universities, hospitals, and large office parks. As employment centers seem to be dependent on zoning, it would be interesting to see how the these centers changed over time in context with zoning changes.

According to `sd_center['total_employees'].sum()` these centers contain a total of **422,216** employees.

### Riverside

We find roughly 7 employment centers in Riverside. It should be noted that our methods identify 9 separate employment centers in Riverside, but we can assume that some of them are apart of the same center due to their proximity.
1. Downtown San Bernadino
2. Downtown Riverside
3. A portion of western Riverside
4. Ontario
5. Downtown Corona
6. Chino
7. A portion of western Upland

In this region, it seems that many of the employment centers are located in areas with high amounts of Transportation and Warehousing, or in the downtown centers with large amounts of government administration.

According to `rv_center['total_employees'].sum()`  these centers contain a total of **313,403** employees.

## Next Steps

1. Analyze employment centers over time in context with transportation improvements and zoning changes in the region.
2. Analyze change in employment share within these centers over time.