---
title: "A Computational Approach for Defining Metropolitan Employment Centers:  Polycentric Urban Form & the p-Regions Problem"
author:
- name: Elijah Knaap
  affiliation: University of California-Riverside
  email: knaap@ucr.edu
- name: Ran Wei
  affiliation: University of California-Riverside
  email: ranwei@ucr.edu
- name: Sergio Rey
  affiliation: University of California-Riverside
  email: serge.rey@ucr.edu
date: January 2020
abstract: >-
    Recent work has suggested a departure from the familiar monocentric city model
    popularized into a polycentric urban form defined by multiple
    employment centers that form along regional transportation corridors.
    Importantly, these studies have demonstrated the
    ways in which the forces of localization and agglomeration can work together to
    define a pallette of well-defined employment centers that may specialize in
    certain industries but nonetheless increase the economic performance of firms
    that choose to locate inside Despite the important advances in polycentric
    research, we know little about the properties of these employment centers across
    the range of metropolitan regions, since the existing research has been
    constrained to a handful of large metropolitan regions. Thus, in this paper, we
    employ a novel modification of the max-p algorithm by extending it to
    incorporate two threshold constraints (satisfying both total employment and
    density thereof) and applying our method to every metropolitan region in the
    United States. By leveraging the max-p algorithm we uncover the polycentric
    urban form in each of America's metropolitan regions and describe the size,
    shape, and composition of the resulting employment centers. Using these results,
    we describe how the identified employment centers can be leveraged as the basis
    of economic development, sustainability, and equitable transportation planning.
bibliography: paper/references.bib
---

# Introduction

Over the last several decades, American metropolitan regions have borne witness
to major economic restructuring as the American economy has shifted from
manufacturing and XXX to a service and knowledge-based economy. Concurrent with
these trends is a less severe but equally important restructuring of the
*spatial structure* of American employment, as certain industries have begin
gravitating toward more suburban locations to be nearer to their employment
bases, whereas other industries are flocking to inner cities. These trends
suggest a critical reckoning for the study of agglomeration economies that
provides the foundation of modern urban economics and regional science. Recent
work has suggested a departure from the familiar monocentric city model
popularized by @Muth1969 into a polycentric urban form defined by multiple
employment centers that form along regional transportation corridors
[@Knaap2016;@Giuliano1991]. Importantly, these studies have demonstrated the
ways in which the forces of localization and agglomeration can work together to
define a pallette of well-defined employment centers that may specialize in
certain industries but nonetheless increase the economic performance of firms
that choose to locate inside. Furthermore, more recent evidence has demonstrated
that these employment centers also provide a range of benefits for achieving
global sustainability such as reduced transportation costs and lower trip
durations.

Despite the important advances in polycentric research, we know little about the
properties of these employment centers across the range of metropolitan regions,
since the existing research has been constrained to a handful of large
metropolitan regions. Existing work often adopts a relatively simple definition
of an employment center: a set of contiguous spatial units whose combined total
employment and employment density meet some pre-defined thresholds. But this process
of identifying employment centers is prohibitively laborious, since it requires
the tedious and iterative process of aggregating spatial units, testing whether
each constraint is met, then re-aggregating and testing again. Luckily, over the
last decade, a family of "regionalization" algorithms has grown from the
tradition of spatial optimization which excels at identifying the maximum number
of *p*-distinct regions [@Duque2011a] in a spatial dataset. Thus, in this paper,
we employ a novel modification of the max-p algorithm by extending it to
incorporate two threshold constraints (satisfying both total employment and
density thereof) and applying our method to every metropolitan region in the
United States [@duque_max-p-regions_2012]

As a result, we identify a set of American employment centers at a national
scale. By leveraging the max-p algorithm we uncover the polycentric urban form
in each of America's metropolitan regions and describe the size, shape, and
composition of the resulting employment centers. Using these results, we
describe how the identified employment centers can be leveraged as the basis of
economic development, sustainability, and equitable transportation planning.

# Spatial Structure as a Vehicle for Urban Policy

Large portions of urban planning, regional science, and economic geography research are devoted to understanding how spatial patterns like development intensity and the separation of land uses influence social and economic activities. Part of this work is focused on patterns like urban sprawl, and the effect they have on GHG emissions, housing prices, and social welfare. Another--much older--portion of this work focuses
on measuring form to understand the optimal location of resources to maximize economic output

Regardless of the perspective, the literature from across the many disciplines makes clear that urban policy measures are often designed to reshape urban form explicitly, or to make the most of existing form to capitalize on the social, economic, and environmental benefits.


## The Monocentric Model

von thunen, muth, mills, brueckner; agglomeration as a foundation of urban economic and economic development policy. 

public transportation and transportation efficiency more generally  


## Polycentric Urban Development

More recently, especially in newer cities like LA, polycentrism rather than monocentrism is the norm. Giuliano & small show this works well for economic development. On the other hand public transportation is notoriously difficult in LA because its so spread out. (More rencnt eamples of it working??)

In DC, and Baltimore, polycentrism seems to work for both economic development *and* transportation, with cascading environmental benefits as a result @Knaap2016

So polycentrism is not only an important and useful model for encouraging both growth and sustainability, but it also may be emerging as the dominant urban form in the US and across the world.

# Urban Spatial Structure as a *p*-Regions problem

the p-regions problem
@Duque2011a

max-p is a particular version of the problem
@duque_max-p-regions_2012

recently a number of extensions to max-p have been explored
@She2017
@Duque2017

@Li2014 the p-compact-regions problem for urban economic modeling

Here, we propose a novel extension of the max-p regions *idea*. In this case, the modification is 

# Modifying Max-p to Identify Urban Polycenters

In the original formulation of the p-regions problem, a study area is comprised of a set of polygons that must be aggregated to form the largest number of aggregate regions, subject to certain constraints. Here, every unit in the study area should be assigned to a particular region until the study space is partitioned fully. In the case of identifying employment centers, however, the original p-regions formulation requires two important extensions. First it is not appropriate to partition the entire study space 

In the classic max-p problem, regions are identified by (1) satisfying a threshold constraint, and (2) optimizing some objective function, which is typically multivariate similarity among the enclave's attributes. When identifying employment centers, however, this objective function assumes the form of a second constraint; here the alogirthm must satisfy the total employment constraint within the region, but also must satisfy an employment density criterion. 

If we take employment density as the objective to optimize

# Polycentric Urban Form in American Metropolitan Regions

## Quantity, Shape, and Configuration

- radial centers around a central blob (i.e. new centers along transportation corridors extending from an original mono center a la baltimore)?
  - long and extended along transpo lines? (like I-270)
  - round and compact in walkable dense nodes? (like bethesda)
- distinct subnodes without an original center (a la LA?)

- relationship between city size, population size, or econommy size and number of centers?

## Composition

## Evolution over time ??? 

(this would be really cool but would extend the scope a lot)

# Discussion & Policy Implications

# Conclusion

# References
