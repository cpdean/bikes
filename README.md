
## Looking at bike data

At pycon 2013 in Montreal, Julia Evans gave a [talk](http://nbviewer.ipython.org/github/jvns/talks/blob/master/mtlpy35/pistes-cyclables.ipynb) on using iPython Notebook, pandas, and matplotlib to explore Montreal bike and weather data.  I liked the example-focused style and the exploratory narrative, and I really wish that it was more of a standard.

I'm doing the same thing for data from a minneapolis bike share, and trying to create the same example-focused and exploratory style of narrative for not only basic exploration, but also data munging and visualization.


### Timeline

* **2014-09-27** - added voronoi work-in-progress with some click behaviors `projections/see_stations/voronoi/index.html`
* **2014-09-27** - documentation and outlining project history
* **2014-09-07** - fix zoom behavior in `projections/station_flow/index.html`
* **2014-09-06** - fix work-in-progress vis `projections/station_flow/index.html`, didn't understand the math to draw shapes between stations. still don't, to be honest. 
* **2014-08-17** - use pandas dataframes to concisely compute the aggregate bikeflow between a chosen station and the other stations over the course of the year. vis in `projections/station_flow/index.html`
* **2014-08-12** - first d3.js vis.  `data/openstreet/demos/just_points_demo/index.html` took raw station metadata and plotted points on the screen.  Not very useful yet, because i have only station data on the screen. need to figure out how to put additional map data for sense of context.
* **2014-08-04** - started `Tracking Rebalances.ipynb` project.  started with basic visualizations of unprocessed data, but then came up with the domain definition of a "station budget", reprocessed and visualized the new term to demonstrate commuter flow in and out of a given station throughout the course of the year.
* **2014-07-13** - added `basics.ipynb`, exploring simple features of the bike transaction dataset and some examples of projecting data out for later visualizations in d3

