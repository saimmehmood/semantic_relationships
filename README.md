# Learning Semantic Relationships of Geographic Areas based on Trajectories 
A set of tools to understand semantic and geographical proximity between different geographical regions. 
#### accepted research track paper for IEEE Mobile Data Management 2020

### Abstract
Mining trajectory data to find interesting patterns is of increasing research interest due to a broad range of useful applications, including analysis of transportation systems, location-based social networks, and crowd behavior. The primary focus of this research is to leverage the abundance of trajectory data to automatically and accurately learn *latent semantic relationships* between different geographical areas (e.g., semantically correlated neighborhoods of a city) as revealed by patterns of moving objects over time. While previous studies have utilized trajectories for this type of analysis at the level of a single geographical area, the results cannot be easily generalized to inform *comparative analysis* of different geographical areas. In this paper, we study this problem systematically. First, we present a method that utilizes trajectories to learn low-dimensional representations of geographical areas in an embedded space. Then, we develop a statistical method that allows to quantify the degree to which real trajectories deviate from a theoretical *null model*. The method allows to (a) distinguish *geographical proximity* to *semantic proximity*, and (b) inform a comparative analysis of two (or more) models obtained by trajectories defined on different geographical areas. This deep analysis can improve our understanding of how space is perceived by individuals and inform better decisions of urban planning. Our experimental evaluation aims to demonstrate the effectiveness and usefulness of the proposed statistical method in two large-scale real-world data sets coming from the New York City and the city of Porto, Portugal, respectively. The methods we present are generic and can be utilized to inform a number of useful applications, ranging from location-based services, such as point-of-interest recommendations, to finding semantic relationships between different cities.

#### Datasets
 - folder **datasets** contains uniformly randomly sampled 10000 trajectories for 
*new york* - created using Google Directions API by taking starting and ending points of taxi rides,
 and *porto* - obtained from https://archive.ics.uci.edu/ml/datasets/Taxi+Service+Trajectory+-+Prediction+Challenge,+ECML+PKDD+2015. 
 
#### Code
 - folder **code** contains *uniform_grid.py* that generates a uniform grid 
by taking diagonal coordinates for the geographical space.

 - *postgre.sql* contains postgres/postgis queries to store trajectories and geographical area grid cells into
 the database and convert trajectory from set of geospatial coordinates into set of grid cells.

 - *new_york_taxi.py* contains code for fetching trajectory paths through Google Directions API
 by providing starting and ending points taxi rides taken in the area of Manhattan.
#### Acknowledgments
This repo was helpful in writing code to fetch POIs from Google API: (https://github.com/slimkrazy/python-google-places)

Trajectory fetching code was written with the help of Jay: (https://github.com/jaycenca)

For plotting functionality, this repo was helpful: (https://github.com/vgm64/gmplot)
