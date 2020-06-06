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

2. `SDCounty.ipynb` and `RVCounty.ipynb`
   
   These notebooks utilize the GeoJSON files created in the last step to generate interactive visualizations displaying total employment of each center as well as the ability to create visualizations of each NAICS code with its corresponding Location Quotient from the `pf.graph_codes` function.

## Results:

After running all the notebooks, we're left with a set of polygons that define regional employment centers in both Riverside and San Diego. As previously stated, RVCounty.ipynb and SDCounty.ipynb have interactive maps displaying these centers and the ability to display by NAICS code.

### San Diego

We find xxx employment centers in SD. They are located in.....

they contain a total of XXXX employees

### Riverside

## Next Steps

1. first
2. second
3. third