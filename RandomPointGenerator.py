import pandas as pd
import numpy as np
import os
import sys
import NearestNeightbourModular as NNM

# Function to load and get min-max for each column
def get_min_max_values():
    df_numeric = pd.read_excel(os.path.join(sys.path[0], 'HiremasterAI.xlsx'), sheet_name='Sheet1', usecols='K:S')
    df_binary = pd.read_excel(os.path.join(sys.path[0], 'HiremasterAI.xlsx'), sheet_name='Sheet1', usecols='T:AB')
    
    # Assuming binary columns should not be randomized as they are categorical
    min_max_values = df_numeric.agg(['min', 'max']).to_dict()

    return min_max_values

# Function to generate a random data point
def generate_random_data_point(min_max_values):
    random_data_point = {}
    for col, min_max in min_max_values.items():
        min_val, max_val = min_max['min'], min_max['max']
        # Generate a random number within the range for numeric columns
        random_data_point[col] = np.random.uniform(min_val, max_val) if pd.notnull(min_val) else np.nan
    
    # Add binary values as well, change this if you want randomization for these as well
    random_data_point.update({
        'Date Info': np.random.choice([0, 1]),
        'Location Info': np.random.choice([0, 1]),
        'Salary Mentioned': np.random.choice([0, 1]),
        'Job Description': np.random.choice([0, 1]),
        'Skills Required': np.random.choice([0, 1]),
        'Qualifications Desired': np.random.choice([0, 1]),
        'Company Overview': np.random.choice([0, 1]),
        'Mentions Benefits': np.random.choice([0, 1]),
        'Has Logo': np.random.choice([0, 1])
    })

    return random_data_point

# Use this main function to test the random data point generation
def main():
    min_max_values = get_min_max_values()
    random_data_point = generate_random_data_point(min_max_values)
    print(random_data_point)
    NNM.predict_new_data_point(random_data_point)

if __name__ == "__main__":
    main()
