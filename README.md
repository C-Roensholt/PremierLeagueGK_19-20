# Analysis of the Goalkeeper in the 2019/2020 Season

This repository consists of an analysis of all the goakeepers in the Premier League who had recorded more than 6 games. The analysis goes beyond common metrics like Save Percentage and Clean Sheets. With the use of StatsBomb's Expected Goals model, I'll cover metrics like Post Shot Expected Goals +/-, Goals Saved Above Average (GSAA) and Goals Saved Above Expectation (GSAE).

This analysis is conducted with inspiration by José Pérez (https://twitter.com/jcperez_?lang=da).

## Content

* **notebooks**
    * **part1_basicMetrics.ipynb** discusses some basic metrics within the goalkeeping analytics scene. In this notebook we cover clean-sheets and saves (like save percentage, saves per match etc.). It is discussed how these metrics can't evaluate a goalkeepers performance alone and we quickly tease for a more reliable evaluation metric, Post Shot expected Goal (PSxG). 

    * **part2_advancedMetrics.ipynb** consists of an analysis of more advanced metrics regarding save percentage, which are more precise in the evaluation of goalkeepers performance. These are Expected Save Percentage (xSv%) and Adjusted Save Percentage (aSv%).Especially aSv% is a metric/visualization which, in my opinion is the best metric in goalkeeper analytics.

    * **part3_advancedMetrics.ipynb** includes a description of Goals Saved Above Average and Goals Saved Above Expectation. These are two well known metrics within the goalkeeper analytics in other sports, especially ice hockey.


* **data**

This folder holds all, and even additional, data which is used in the creation of all the metrics and visualizations. The data is provided by **StatsBomb** through the website [fbref.com](https://fbref.com/en/). The data is all goalkeeper from the 2019/2020 season in the Premier League. Additional I've downloaded the same data from the other four major leagues in Europe in the intention of exploring and do an analysis of the other leagues in Europe.

* **output**

The _output folder_ consists of all the visualization which is created from the notebooks.

* **plots**

This folder includes some basic templates of the visualizations created throughout this _"project"_. Including barplots, scatterplots, bubbleplots etc.