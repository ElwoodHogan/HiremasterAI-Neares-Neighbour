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
df = pd.read_excel(os.path.join(sys.path[0], 'HiremasterAI.xlsx'), sheet_name='Sheet1', usecols='K:Q')
print("read")




# Exclude the first three attributes from the comparison
#df = df.drop(columns=['Company', 'Link', 'Revenue', 'Headline', 'subheadline','Body copy', 'trust', 'indicators', 'call to action', '\"me too\" factor'])

# Step 2: Feature Engineering
# For demonstration, let's assume 'headline', 'subheadline', 'body copy' are text fields,
# and the rest are either numerical or can be directly used.
vectorizers = {}
tfidf_columns = []


# Separate columns by type for easier processing
#string_cols = ['trust', 'indicators', 'call to action', '"me too" factor', 'primary color', 'secondary color']
int_cols = ['Word Count', 'Character Count', 'Bullet Point Count']
string_cols =  [col for col in df.columns if col not in int_cols]
#['Primary color', 'Secondary color', , 'Location Info' ]:

# Impute missing values
imputer = SimpleImputer(strategy='mean')
df[int_cols] = imputer.fit_transform(df[int_cols])

# Label encode string columns and keep track of the encoders
label_encoders = {}
placeholder = 'UNKNOWN'
for col in string_cols:
    le = LabelEncoder()
    df[col] = df[col].astype(str)
    df[col] = df[col].apply(lambda x: x if x != 'nan' else placeholder)
    le.fit(df[col])
    label_encoders[col] = le

# Optionally, scale integer columns
scaler = StandardScaler()
df[int_cols] = scaler.fit_transform(df[int_cols])

# Convert DataFrame to NumPy array
X = df.to_numpy()

# Step 3: Model Building
knn = NearestNeighbors(n_neighbors=3)
knn.fit(X)

# Step 4: Prediction
# Prepare the new data point
new_point = {
    'Primary color': 'white',
    'Secondary color': 'pink',
    'Word Count': '500',
    'Character Count' : '8000',
    'Bullet Point Count' : '5',
    'Date Info' : 'yes',
    'Location Info' : 'yes'
    # ... other attributes ...
}

# Convert unseen categories to placeholder and apply transformations
for col in string_cols:
    if new_point[col] not in label_encoders[col].classes_:
        new_point[col] = placeholder
    new_point[col] = label_encoders[col].transform([new_point[col]])[0]

# Create a NumPy array from new_point
new_point_array = np.array([new_point[col] for col in df.columns]).reshape(1, -1)

# Run k-NN prediction
distances, indices = knn.kneighbors(new_point_array)

print(f"Nearest neighbors indices: {indices}")
print(f"Distances to nearest neighbors: {distances}")