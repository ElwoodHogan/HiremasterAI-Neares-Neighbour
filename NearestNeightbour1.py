import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os
import sys
import numpy as np
from sklearn.impute import SimpleImputer

print(str(os.path.join(sys.path[0], 'HiremasterAI.xlsx')))

# Step 1: Data Preprocessing
# Load Excel file into a DataFrame
df_numeric = pd.read_excel(os.path.join(sys.path[0], 'HiremasterAI.xlsx'), sheet_name='Sheet1', usecols='K:S')

# Import new columns and convert 'yes'/'no' to binary
df_binary = pd.read_excel(os.path.join(sys.path[0], 'HiremasterAI.xlsx'), sheet_name='Sheet1', usecols='T:AB')
binary_map = {'yes': 1, 'no': 0}
df_binary = df_binary.applymap(lambda x: binary_map.get(str(x).lower(), x) if isinstance(x, str) else x)


# Concatenate the binary DataFrame with the numeric DataFrame
df = pd.concat([df_numeric, df_binary], axis=1)


# Step 2: Feature Engineering
# For demonstration, let's assume 'headline', 'subheadline', 'body copy' are text fields,
# and the rest are either numerical or can be directly used.
vectorizers = {}
tfidf_columns = []



# Separate columns by type for easier processing
string_cols = []
int_cols =  [col for col in df.columns if col not in string_cols]
#['Primary color', 'Secondary color', , 'Location Info' ]:

# Impute missing values
imputer = SimpleImputer(strategy='mean')
df[int_cols] = imputer.fit_transform(df[int_cols])

# Optionally, scale integer columns
#scaler = StandardScaler()
#df[int_cols] = scaler.fit_transform(df[int_cols])

# Convert DataFrame to NumPy array
X = df.to_numpy()

# Step 3: Model Building
knn = NearestNeighbors(n_neighbors=3)
knn.fit(X)

# Step 4: Prediction
# Prepare the new data point
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


# Create a NumPy array from new_point
new_point_array = np.array([new_point[col] for col in df.columns]).reshape(1, -1)

# Run k-NN prediction
distances, indices = knn.kneighbors(new_point_array)

print(f"Nearest neighbors indices: {indices}")
print(f"Distances to nearest neighbors: {distances}")