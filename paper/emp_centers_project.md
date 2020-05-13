# Urban Employment Centers

An employment center is a place of extremely dense (read: "accessible") employment--e.g. "starting
at the intersection of 5th and Main, there are 35,000 jobs within a 15 minute walk. It's important to understand where these centers are and how they're evolving because they have a big impact on equity, economy, environment. For these reasons, we want to know a variety of information about each center:

- what is the location and spatial extent of each center?
- how diverse or specialized are the jobs in each?
- how does the infrastructural and architectural environment differ in each center?

Studying these questions can inform important urban policy questions such as:

- should we [subsidize Amazon](https://theintercept.com/2018/11/15/amazon-hq2-long-island-city-virginia-subsidies/) to move in?
    - what about [under armour?](https://www.washingtonpost.com/news/digger/wp/2016/09/20/baltimore-approves-660-million-for-under-armour-development/)
- who would gain job access if we investede in a new Bus Rapid Transit line?
- how much job growth could we expect if we upzoned downtown and added a dedicated bike lane?
- what would happen if we [closed broadway](https://slate.com/human-interest/2009/06/is-closing-broadway-to-cars-good-for-times-square.html) to cars?

The answers to these questions require us to compare the characteristics of centers to one another, to themselves over time, and to employment *outside* of centers using a wide variety of metrics categorized according to the overarching questions posed above

## Spatial Footprint

To understand the spatial footprint of each employment center, we need to calculate access to jobs from each neighborhood in our study area. If a neighborhood meets a certain threshold of access, it's considered a center (and any neighborhood that also meets the threshold and shares a side or vertex is considered part of the same center). Using data from OSM, and GTFS along with tools like [pandana](https://github.com/UDST/pandana), anyone interested in this component of the project will help calculate accessibility measures and identify employment centers. After the centers are identified, further metrics for calculate include:

- total employment in each center
- total area in each center
- employment density across centers
- change in these metrics over time

Before calculating these measures, it will be necessary to define important theoretical parameters such as the distance/commute time used to calculate accessibility, the number of jobs that defines the cutoff for identifying a center, and what kinds of networks should be included. An additional area for research might be exploring alternative scenarios generated from changing the transit infrastructure.

## Industrial Composition

To understand the characteristics of job specialization, competition, and growth, we need to calculate measures related to the employment composition in each center. These help us understand questions such as which centers are characterized by [urbanization versus localization](https://en.wikipedia.org/wiki/Localization_and_Urbanization_Economies). Anyone interested in this project will use LEHD and tools like the pysal [segregation](https://github.com/pysal/segregation/blob/master/notebooks/local_measures_example.ipynb) package data to calculate measures of the local economy such as

- Herfindahl index
- shift share analyses
- location quotient
- Simpson's diversity

## Urban Form

To understand how characteristics of the built environment influence economic growth and performance, we also need measures of urban morphology. These metrics help us understand how a particular site can attract development due to design elements, or distinctive character that contributes to a unique functionality, visual character, navigability, or efficiency. Anyone in this aspect of the project will help collect data from OSM and use tools such as [momepy](https://guide.momepy.org/combined/distribution) to calculate measures like

- the shape and orientation of buildings and streets in each center
- the alignment and setback of buildings relative to streets
- building intensity, such as coverage-area ratio (CAR) or floor-area-ratio (FAR)
- interbuilding distance
- street network measures
  - intersection centrality
  - mean connectivity