import pandas as pd

#Question 1: How did the number of land birds vs. pelagic birds collected change over time? 

#The data would first need to count the number of each bird group collected on each day because currently the data shows every bird collected. 
#Using a two sample t-test, the list can be used to compare the amount of birds of each group collected at the beginning of the datasheet
#to the end of the collection period.

# First need to convert data in DeadCollectedBirds_Dataset.csv file to numerical data (use panda)
data = pd.read.csv(.../DeadCollectedBirds_Dataset.csv)

# Add a variable for each useful column in the dataset
#I'm not sure if the data[] function is the best to use here since a lot of these are names or times
# also idk if the column names are the right format. the other assignment that i did this for had no spaces in the column name
Date = data['Date Collected']
Extrapolation_Area = data['Extrapolation Area']
Region_Name = data['Region Name']
State = data['State']
Species = data['Species']
Bird_Group = data['Bird Group']
Position = data['Position']
Scavenging = data['Scavenging']
Time Collected = data['Time Collected']
