import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#Question 1: How did the number of land birds vs. pelagic birds collected change over time? 

#The data would first need to count the number of each bird group collected on each day because currently the data shows every bird collected. 
#Using a two sample t-test, the list can be used to compare the amount of birds of each group collected at the beginning of the datasheet
#to the end of the collection period.

print("Question 1: Land Birds vs Pelagic Birds (monthly totals)")

def analyze_question_1(filepath):
    # Read the dataset using pandas:
    data = pd.read_csv(filepath, encoding='utf-8-sig')

    print(data.columns.tolist())
    
    # Convert 'Date Collected' to datetime and create a year/month column:
    data['Date Collected'] = pd.to_datetime(data['Date Collected'], errors='coerce')
    data['YearMonth'] = data['Date Collected'].dt.to_period('M').astype(str)

    # Remove rows without a valid collection date
    data = data.dropna(subset=['Date Collected'])

    # Create a column identifying the month and year
    data['YearMonth'] = data['Date Collected'].dt.to_period('M')
 
    # Filter for land birds vs pelagic birds using 'BirdGroup':
    land_df = data[data['BirdGroup'].str.lower().str.contains('land', na=False)]
    pelagic_df = data[data['BirdGroup'].str.lower().str.contains('pelagic', na=False)]

    # Count number of birds collected on each month:
    land_monthly = land_df.groupby('YearMonth').size().reset_index(name='Land_Count') 
    pelagic_monthly = pelagic_df.groupby('YearMonth').size().reset_index(name='Pelagic_Count') 

    # Combine both groups into one table
    merged_monthly = pd.merge(land_monthly, pelagic_monthly,on='YearMonth', how='outer').fillna(0)

    # Sort the data chronologically
    merged_monthly = merged_monthly.sort_values('YearMonth')

    print(merged_monthly.to_string(index=False))

    # Compare first half vs second half of timeline using t-test:
    midpoint = len(merged_monthly) // 2
    if midpoint > 1:
        # land bird t-test
        land_beginning = merged_monthly['Land_Count'].iloc[:midpoint]
        land_end = merged_monthly['Land_Count'].iloc[midpoint:]

        t_stat, p_value = stats.ttest_ind(land_beginning, land_end)
        print()
        print(f"Two-Sample T-Test(Beginning vs End Collection) -> t-stat: {t_stat:.4f}, p-value: {p_value:.4f}")

        t_land, p_land = stats.ttest_ind(land_beginning, land_end, equal_var=False)

        # Pelagic bird t-test
        pelagic_beginning = merged_monthly['Pelagic_Count'].iloc[:midpoint]
        pelagic_end = merged_monthly['Pelagic_Count'].iloc[midpoint:]

        t_pelagic, p_pelagic = stats.ttest_ind(pelagic_beginning, pelagic_end, equal_var=False)

        print("\n=== T-Test Results ===")
        print(f"Land Birds: t = {t_land:.4f}, p = {p_land:.4f}")
        print(f"Pelagic Birds: t = {t_pelagic:.4f}, p = {p_pelagic:.4f}")


    # Create a plot comparing both bird groups over time
    plt.figure(figsize=(10, 6))

    plt.plot(
        merged_monthly['YearMonth'].astype(str),
        merged_monthly['Land_Count'],
        label='Land Birds',
        marker='o'
    )

    plt.plot(
        merged_monthly['YearMonth'].astype(str),
        merged_monthly['Pelagic_Count'],
        label='Pelagic Birds',
        marker='o'
    )

    plt.xlabel('Month')
    plt.ylabel('Number of Birds Collected')
    plt.title('Land Birds vs. Pelagic Birds Collected Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Run the function
if __name__ == "__main__":
    analyze_question_1('DeadCollectedBirds_Dataset.csv')
