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



#====this is how I did question 1, let me know if looks good same for question 2====#

import pandas as pd 
from scipy import stats

def analyze_question_1(filepath):
    # Read the dataset using pandas:
    data = pd.read_csv(filepath, encoding='Latin-1')
   
    # Convert 'Date Collected' to datetime and create a year/month column:
    data['Date Collected'] = pd.to_datetime(data['Date Collected'], errors='coerce')
    data['YearMonth'] = data['Date Collected'].dt.to_period('M').astype(str)
 
    # Filter for land birds vs pelagic birds using 'BirdGroup':
    land_df = data[data['BirdGroup'].str.lower().str.contains('land', na=False)]
    pelagic_df = data[data['BirdGroup'].str.lower().str.contains('pelagic', na=False)]

    # Group by month to get realistic collection volumes:
    land_monthly = land_df.groupby('YearMonth').size().reset_index(name='Land_Count') 
    pelagic_monthly = pelagic_df.groupby('Date Collected').size().reset_index(name='Pelagic_Count')

    # Count number of birds collected on each month:
    land_monthly = land_df.groupby('YearMonth').size().reset_index(name='Land_Count') 
    pelagic_monthly = pelagic_df.groupby('YearMonth').size().reset_index(name='Pelagic_Count') 

    merged_monthly = pd.merge(land_monthly, pelagic_monthly, on='YearMonth', how='outer').fillna(0)
    merged_monthly = merged_monthly.sort_values('YearMonth') 

    print("=== Question 1: Land Birds vs Pelagic Birds (monthly totals) ===")
    print(merged_monthly.to_string(index=False))

    # Compare first half vs second half of timeline using t-test:
    midpoint = len(merged_monthly) // 2
    if midpoint > 1:
        beginning = merged_monthly['Land_Count'].iloc[:midpoint]
        end = merged_monthly['Land_Count'].iloc[midpoint:]

        t_stat, p_value = stats.ttest_ind(beginning, end)
        print()
        print(f"Two-Sample T-Test(Beginning vs End Collection) -> t-stat: {t_stat:.4f}, p-value: {p_value:.4f}")

if __name__ == "__main__":
    #replace with your own csv file 
    analyze_question_1(......./..... .csv)
