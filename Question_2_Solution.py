import pandas as pd
from scipy import stats

def analyze_question_2(filepath):
    # Read the dataset using pandas
    data = pd.read_csv(filepath, encoding='latin-1')
    """
    Question 2: what area were the rail birds and raptor birds scavenged the most?
    Uses 'Extrapolation Area', 'Scavenging', and 'Bird Group'.
    """
    # Filter for rail and raptor birds using 'BirdGroup'
    rail_mask = data['BirdGroup'].str.lower().str.contains('rail', na=False)
    raptor_mask = data['BirdGroup'].str.lower().str.contains('raptor', na=False)
    
    rail_df = data[rail_mask]
    raptor_df = data[raptor_mask]
 
    # Group by Extrapolation Area and count scavenging instances
    rail_scavenging = rail_df.groupby('Extrapolation Area').size()
    raptor_scavenging = raptor_df.groupby('Extrapolation Area').size()
    
    print("=== Question 2: Scavenging Analysis ===")
    print("\nRail Birds- Scavenging by Extrapolation Area:")
    print(rail_scavenging)

    print("\nRaptor Birds- Scavenging by Extrapolation Area:")
    print(raptor_scavenging)

    # One-sided T-Test comparing area totals
    if len(rail_scavenging) > 1 and len(raptor_scavenging) > 1:
        t_stat, p_value = stats.ttest_ind(rail_scavenging, raptor_scavenging, alternative='greater')
        print()
        print(f"One-Sided T-Test(Rail vs Raptor Area Scavenging) -> t-stat: {t_stat:.4f}, p-value: {p_value:.4f}")

if __name__ == "__main__":
    #replace with your own csv file 
    analyze_question_2(....../.... .csv)
