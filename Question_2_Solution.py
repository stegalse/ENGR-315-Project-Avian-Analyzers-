import csv
from collections import defaultdict
from scipy import stats

def analyze_question_2(filepath):
    """
    Question 2: what area were the rail birds and raptor birds scavenged the most?
    Uses 'Extrapolation Area', 'Scavenging', and 'BirdGroup'.
    """
    rail_birds = []
    raptor_birds = []
    
    # Store counts by area and scavenging condition:
    rail_scavenging_by_area = defaultdict(lambda: defaultdict(int))
    raptor_scavenging_by_area = defaultdict(lambda: defaultdict(int))

    with open(filepath, mode='r', encoding='latin-1') as file: 
        reader = csv.DictReader(file)
        for row in reader:
            # Using exact column names from datasheet:
            bird_group = row.get('BirdGroup', '').strip().lower()
            area = row.get('Extrapolation Area', '').strip()
            scavenging = row.get('Scavenging', '').strip().lower()
          
            if 'rail' in bird_group:
                rail_birds.append((area, scavenging))
                if area and scavenging:
                    rail_scavenging_by_area[area][scavenging] += 1
            elif 'raptor' in bird_group:
                raptor_birds.append((area, scavenging))
                if area and scavenging:
                    raptor_scavenging_by_area[area][scavenging] +=1 

    print("=== Question 2: Scavenging Analysis ===")

    # Finding the area with the most scavenging observations for Rail birds:
    print("\nRail Birds- Scavenging by Extrapolation Area:")
    for area, conditions in rail_scavenging_by_area.items():
        total_scavenged = sum(conditions.values())
        print(f" Area: {area} -> Total Scavenging Instances: {total_scavenged}")

    # Finding the area with the most scavenging observations for Raptor birds:
    print("\nRaptor Birds- Scavenging by Extrapolation Area:")
    for area, conditions in rail_scavenging_by_area.items():
        total_scavenged = sum(conditions.values())
        print(f" Area: {area} -> Total Scavenging Instances: {total_scavenged}")


    # Performing a one-sided t-test example comparing total scavenging per area between groups:
    rail_totals = [sum(conds.values()) for conds in rail_scavenging_by_area.values()]
    raptor_totals = [sum(conds.values()) for conds in raptor_scavenging_by_area.values()]

    if len(rail_totals) > 1 and len(raptor_totals) > 1:
        t_stat, p_value = stats.ttest_ind(rail_totals, raptor_totals, alternative='greater')
        print(f"One-Sided T-Test(Rail vs Raptor Area Scavenging) -> t-stat: {t_stat:.4f}, p-value: {p_value:.4f}")

if __name__ == "__main__":
    #replace with your own csv file: 
    analyze_question_2(.........../... .csv)
