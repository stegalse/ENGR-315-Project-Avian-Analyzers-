import pandas as pd

#Question 1: How did the number of land birds vs. pelagic birds collected change over time? 

#The data would first need to count the number of each bird group collected on each day because currently the data shows every bird collected. 
#Using a two sample t-test, the list can be used to compare the amount of birds of each group collected at the beginning of the datasheet
#to the end of the collection period.

# First need to convert data in DeadCollectedBirds_Dataset.csv file to numerical data (use panda)
data = pd.read.csv(.../DeadCollectedBirds_Dataset.csv)
