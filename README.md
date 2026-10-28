# ENGR-315-Project-Avian-Analyzers-

Samantha Stegall, Flint Gashaw, Jillian Davis 
Dr. M. Ceylan Morgul
ENGR 315 Computational Methods in Engineering

Project Title: Bird Insights from the Deepwater Horizon Oil Spill
Team Name: Avian Analyzers 

Sub-Task 2: Objective and Motivation
Specify Dataset and provide details
Our group decided to analyze a dataset that recorded the number of dead birds collected by a Natural Resource Damage Assessment group (NRDA) after the Deepwater Horizon (DWH) oil spill. Birds are an important part of any ecosystem for a number of reasons, such as dispersing seeds, controlling pest populations, and pollinating plants. When a catastrophic human error such as an oil spill occurs, it is important to analyze how it affects the environment short- and long-term. Our group cares about the environment and would like to see how an oil spill quantitatively affects the ecosystem, specifically the birds. Most of the data collected was meant to be utilized as part of the avian injury quantification reports, recording information such as the number of birds collected, decomposition of the birds, location of collection, species, and much more. Most of the information that will likely be used for this analysis could be the date and location of collection, collector and collection group, species of bird, and position of the bird.
Dataset: Department of the Interior - DWH NRDA Collected Dead Birds (https://catalog.data.gov/dataset/dwh-nrda-collected-dead-birds?from_hint=eyJxIjoiYmlyZHMiLCJzb3J0IjoicmVsZXZhbmNlIn0%3D) 

Question 1: How did the number of land birds vs. pelagic birds collected change over time? 
Using the date collected, this question could show the long-term effects of oil spills on land and sea birds and how long it takes to fully clean up an oil spill. 
The data would first need to count the number of each bird group collected on each day because currently the data shows every bird collected. Using a two sample t-test, the list can be used to compare the amount of birds of each group collected at the beginning of the datasheet to the end of the collection period. 
Expected answer: 

Question 2: What area were the rail birds and raptor birds scavenged the most? 
This question uses the extrapolation area, scavenging of the birds, and bird groups. This looks at the effect of the oil spill on the small birds and larger, predatory birds in each respective area. 
Answering this question could require a one-sided t-test, comparing the maximum of one area’s skeletal birds to others. 
Expected answer: 

Question 3: What species within each bird group was collected the most? 
By looking at the species and bird group, we can see which species were affected the most by the oil spill. 
This question could likely be answered by counting the number of each species within each group, then comparing those totals to find the maximum number of species within each group. For just the land bird group, either the northern cardinal or pesserine could have been collected the most. 
Expected answer: 


Sub-Task 3 + 4: Implementation Details

Question 1: How did the number of land birds vs. pelagic birds collected change over time?
What metrics will be calculated from the data that will help analysis? (how are we going to answer the question?) 
The metrics calculated are the number of land birds and pelagic birds over time, that data will help analysis because it will allow us to see how the the collected birds changed over the time period they started collecting them. 
Are there any additional python packages that would be useful in analysis? 
What type of plots and visualization would be useful in conveying the final results? 
A plot comparing the number of land vs pelagic birds over time will be useful. It shows clearly the types of birds collected and shows when the spikes are and how the data changes.

Question 2: What area were the rail birds and raptor birds scavenged the most? 
What metrics will be calculated from the data that will help analysis? (how are we going to answer the question?)
Are there any additional python packages that would be useful in analysis? 
What type of plots and visualization would be useful in conveying the final results? 

Question 3: What species within each bird group was collected the most? 
What metrics will be calculated from the data that will help analysis? (how are we going to answer the question?)
The metrics that will be calculated would be the number of each species and what group they belong to. From there that would help us analyze which species of the land birds were most affected and what species of pelagic birds were most affected.
Are there any additional python packages that would be useful in analysis? 
What type of plots and visualization would be useful in conveying the final results? 
Bar graph or pie chart

Sub-Task 6: Results 


Sub-Task 7: Conclusions 


References: 
