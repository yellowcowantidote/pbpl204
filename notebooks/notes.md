# Notes

> We seek a definition that incorporates adjacent high-density zones, and which restricts attention to centers large enough to exert a potentially significant influence. 
@Giuliano1991 p.166

that actually sounds like dbscan. the problem with dbscan is you cant guarantee that you'll have contiguity. What about:

- run dbscan on block centroids with employment as the attribute (so x, y, total employment)
- the resulting assigned points and take their convex hull?

> We therefore define a center as a continuous set of zones, each with density above some cutoff D, that together have at least E total employment and for which all the immediately adjacent zones outside the subcenter have density below D. (To be classified as adjacent, the zones must have at least zones 0.25 miles of common boundary.) With this definition, all high-density zones in the region are classified as part of some center unless they are both small (less than E employment) and isolated (not part of a cluster of high-density zones with E employment in total). The peak of the center is defined as the highest-density zone or group of contiguous zones within the subcenter that together have at least _!? employees.

What about:

- apply a smoother (multiply through kernel W) which gives you the employment surface
- define the horizontal cutoff (a single number now instead of two)
- now you have a different parameter to set - kernel bandwidth


part of the reason the guiliano paper was important, and why we duplicated it, was because it was framed in classic RS terms of *transportation*
They're using TAZs so they can test how many trips ended up in those centers (disaggregated by mode, otherwise its a tautology... if the jobs are there' they're generating trips)