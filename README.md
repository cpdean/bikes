
## Looking at bike data

At pycon 2013 in Montreal, Julia Evans gave a [talk](http://nbviewer.ipython.org/github/jvns/talks/blob/master/mtlpy35/pistes-cyclables.ipynb) on using iPython Notebook, pandas, and matplotlib to explore Montreal bike and weather data.  I liked the example-focused style and the exploratory narrative, and I really wish that it was more of a standard.

I'm doing the same thing for data from a minneapolis bike share, and trying to create the same example-focused and exploratory style of narrative for not only basic exporation, but also data munging and visualization.  While a notebook enforces a linear story that you tell with the data, I haven't yet figured out how to tie all of my side experiments together, so everything is very scattered around.

I want to pull all these drafts together into something more cohesive that people can read and follow along, but for the moment I'll just list changes and experiments chronologically.

### Timeline

* 2014-09-27 - documentation and outlining project history
* 2014-09-07 - fix zoom behavior in `projections/station_flow/index.html`
* 2014-09-06 - fix work-in-progress vis `projections/station_flow/index.html`, didn't understand the math to draw shapes between stations. still don't, to be honest. 
* 2014-08-17 - use pandas dataframes to concisely compute the aggregate bikeflow between a chosen station and the other stations over the course of the year. vis in `projections/station_flow/index.html`
* 2014-08-12 - first d3.js vis.  `data/openstreet/demos/just_points_demo/index.html` took raw station metadata and plotted points on the screen.  Not very useful yet, because i have only station data on the screen. need to figure out how to put additional map data for sense of context.
* 2014-08-04 - started `Tracking Rebalances.ipynb` project.  started with basic visualizations of unprocessed data, but then came up with the domain definition of a "station budget", reprocessed and visualized the new term to demonstrate commuter flow in and out of a given station throughout the course of the year.
* 2014-07-13 - added `basics.ipynb`, exploring simple features of the bike transaction dataset and some examples of projecting data out for later visualizations in d3

