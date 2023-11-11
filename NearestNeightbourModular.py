import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
from sklearn.impute import SimpleImputer
import os
import sys

# Function to load and preprocess data
def load_and_preprocess_data():
    df_numeric = pd.read_excel(os.path.join(sys.path[0], 'HiremasterAI.xlsx'), sheet_name='Sheet1', usecols='K:S')
    df_binary = pd.read_excel(os.path.join(sys.path[0], 'HiremasterAI.xlsx'), sheet_name='Sheet1', usecols='T:AB')
    binary_map = {'yes': 1, 'no': 0}
    df_binary = df_binary.applymap(lambda s: binary_map.get(s.lower(), s) if isinstance(s, str) else s)

    df = pd.concat([df_numeric, df_binary], axis=1)
    imputer = SimpleImputer(strategy='mean')
    df[:] = imputer.fit_transform(df[:])
    
    return df

# Function to create and train the model
def train_knn_model(X):
    knn = NearestNeighbors(n_neighbors=3)
    knn.fit(X)
    return knn

# Function to find nearest neighbors for a new data point
def find_nearest_neighbors(new_point, df, knn):
    new_point_array = np.array([new_point[col] for col in df.columns]).reshape(1, -1)
    distances, indices = knn.kneighbors(new_point_array)
    
    return distances, indices

# Main function to be called with new data point
def predict_new_data_point(new_point):
    df = load_and_preprocess_data()
    knn = train_knn_model(df.to_numpy())
    distances, indices = find_nearest_neighbors(new_point, df, knn)
    
    # Output the results
    print(f"\nNearest neighbors indices: {indices}")
    print(f"Distances to nearest neighbors: {distances}")
    
    for i, index in enumerate(indices[0]):
        print(f"\nNeighbor {i + 1}, at index {index}, distance: {distances[0][i]}")
        print(df.iloc[index])

new_point = {
    'Primary R': 255,
    'Primary G': 255,
    'Primary B': 255,
    'Secondary R': 0,
    'Secondary G': 0,
    'Secondary B': 0,
    'Word Count': 500,
    'Character Count' : 8000,
    'Bullet Point Count' : 5,
    'Date Info' : 0,
    'Location Info' : 1,
    'Salary Mentioned' : 0,
    'Job Description' : 1,
    'Skills Required' : 0,
    'Qualifications Desired' : 1,
    'Company Overview' : 0,
    'Mentions Benefits' : 1,
    'Has Logo' : 0
    # ... other attributes ...
}

#predict_new_data_point(new_point)
