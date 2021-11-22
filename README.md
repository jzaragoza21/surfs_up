# Surfs_Up Analysis

Click here for the challenge code for the analysis: [Surfs_Up_Challenge](https://github.com/jzaragoza21/surfs_up/blob/main/SurfsUp_Challenge.ipynb)

## Overview of Analysis

The objective of this analysis is to execute a basic statistical analysis of Oahu's temperature's in June and December to determine for W. Avywhether a surf and ice cream shop is sustainable year round. In doing so, we use Python and Pandas functions and methods to filter and retrieve temperature data from the hawaii.sqlite database. By crafting queries specifically designed to acquire temperature data, we are able to capture and analyze data such as minimum, maximum and average temperatures for the months of June and December.

## Results

### June Temperature Analysis

The June temperature analysis generated exactly 1,700 observations for the months of June between 2010 and 2017. The average temperature for June in Oahu is 75 degrees while the minimum and maximum temperatures are 64 and 85 degrees respectively. These aforementioned temps coupled with a lower standard deviation of 3.26 indicates there is a small range of temperatures across all June observations. While this sample is across only 7 years, it seems to align with Oahu's overall stable weather. 


![June Temperature Summary Stats](https://github.com/jzaragoza21/surfs_up/blob/main/Resources/June%20Temperature%20Summary%20Stats.png)


### December Temperature Analysis

The December temperature analysis mirrored the June analysis. However, the December analysis only generated 1,517 observations for the months of December between 2010 and 2017, which means there were 183 missing temperature recordings during those years. Nonetheless, we felt the sample size was still sufficient to execute a robust analysis. The summary stats for Decmeber below show that the average is 71 degress while the minimum and maximum temperatures are 56 and 83 degress respectively. As demonstrated, these temperatures and their ranges are similar to June. Additionally, December's standard deviation is also similar in that it is 3.76. Collectively, these two analysis show how stable and similar, albeit from a big picture, Oahu's weather is year round.


![December Temperature Summary Stats](https://github.com/jzaragoza21/surfs_up/blob/main/Resources/December%20Temperature%20Summary%20Stats.png)


## Summary

In analyzing both June and December temperatures, it is clear Oahu's weather is stable year around with the temperatures ranging from 56 to 85 degrees. Based this analysis alone, we would recommend that both a surf shop and ice cream shop would be sustainable year round. Before opening the shop, however, we recommend to additional queries be executed:

1. Precipitation: the frequency and severity of rain would substantially impact a surf shop. We recommend doing this analysis before moving forward with the surf shop.
2. Secondly, we should run a query on weather stations to identify weather patterns and which part of Oahu has the most severe weather activity. Perhaps this could help in idenitfying the most advantageous shop location by filtering down which area has the most stable weather patterns.
