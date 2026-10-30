# ENGR-315-Project-Avian-Analyzers-

Samantha Stegall, Flint Gashaw, Jillian Davis 
Dr. M. Ceylan Morgul
ENGR 315 Computational Methods in Engineering

Project Title: Bird Insights from the Deepwater Horizon Oil Spill
Team Name: Avian Analyzers 

Sub-Task 2: Objective and Motivation
Our group decided to analyze a dataset that recorded the number of dead birds collected by a Natural Resource Damage Assessment group (NRDA) after the Deepwater Horizon (DWH) oil spill. Birds are an important part of any ecosystem for a number of reasons, such as dispersing seeds, controlling pest populations, and pollinating plants. When a catastrophic human error such as an oil spill occurs, it is important to analyze how it affects the environment short- and long-term. Our group cares about the environment and would like to see how an oil spill quantitatively affects the ecosystem, specifically the birds. Most of the data collected was meant to be utilized as part of the avian injury quantification reports, recording information such as the number of birds collected, decomposition of the birds, location of collection, species, and much more. Most of the information that will likely be used for this analysis could be the date and location of collection, collector and collection group, species of bird, and position of the bird.
Dataset: Department of the Interior - DWH NRDA Collected Dead Birds (https://catalog.data.gov/dataset/dwh-nrda-collected-dead-birds?from_hint=eyJxIjoiYmlyZHMiLCJzb3J0IjoicmVsZXZhbmNlIn0%3D) 

Question 1: How did the number of land birds vs. pelagic birds collected change over time? 
Using the date collected, this question could show the long-term effects of oil spills on land and sea birds and how long it takes to fully clean up an oil spill. The data would first need to count the number of each bird group collected on each day because currently the data shows every bird collected. Using a two sample t-test, the list can be used to compare the amount of birds of each group collected at the beginning of the datasheet to the end of the collection period. 

Question 2: What area were the rail birds and raptor birds scavenged the most? 
This question uses the extrapolation area, scavenging of the birds, and bird groups. This looks at the effect of the oil spill on the small birds and larger, predatory birds in each respective area. Answering this question could require a one-sided t-test, comparing the maximum of one area’s skeletal birds to others. 

Question 3: What species within each bird group was collected the most? 
By looking at the species and bird group, we can see which species were affected the most by the oil spill. 
This question could likely be answered by counting the number of each species within each group, then comparing those totals to find the maximum number of species within each group. For just the land bird group, either the northern cardinal or pesserine could have been collected the most. 


Sub-Task 3 + 4: Implementation Details

Question 1: How did the number of land birds vs. pelagic birds collected change over time?
Metrics to be calculated from the data: 
The number of land birds and pelagic birds over time, that data will help analysis because it will allow us to see how the collected birds changed over the time period they started collecting them. Would need to make a list for each tuple (or bird) for each bird group (should make two lists for each bird group). Then create an if/else statement to count the number of land and pelagic birds collected on each date throughout the dataset. Then a two sample t-test could be used to compare the average number of birds collected throughout the collection period. 
No additional python packages would be useful for analysis. 
A plot comparing the number of land vs pelagic birds over time will be useful. It would visually show how the number of each bird group collected changes over time. 


Question 2: What area were the rail birds and raptor birds scavenged the most? 
Metrics to be calculated from the data: 
Similarly to Question 1, a list would need to be made of tuples for each collection of rail birds and raptor birds (2 lists total). Then, an if/elif statement would need to be written to count the number of each type of scavenged bird collected (freshly dead, no scavenging, lightly scavenged, heavily scavenged, mummified). This statement would need to include the area of each collection in the tallying. Using this information, a one sided t-test could be performed to compare the level of scavenging for each bird in each area, then perform another to compare the results from each bird. 
No additional python packages would be useful for analysis. 
Could make plots similar to one in Question 1 that shows the scavenging level in each area for each bird. 


Question 3: What species within each bird group was collected the most? 
Metrics to be calculated from the data: 
The metrics that will be calculated would be the number of each species and what group they belong to. From there that would help us analyze which species of the land birds were most affected and what species of pelagic birds were most affected.
Would first need to make separate lists for each bird group. An if/elif statement would then need to be created to count the number of birds in each species within each group. Then, another if/else statement would need to be made to compare the count for each species, where the species with the highest count would eventually be printed for each bird group. 
We could look at populations for each species to see how the oil spill affected the bird populations, but that is not really necessary. It could add a level of complexity if needed. 
A bar graph showing the species collected the most within each bird group could be a useful visual representation of the dataset. 


Sub-Task 6: Results 



Sub-Task 7: Conclusions 
Actions to be completed (after this phase): 
- Add dataset to repo
- Convert dataset to list with useable data
- Start answering questions
- Start with Q3 b/c it will likely be the easiest to answer

No issues encountered yet. 


References: 
