"""
We have the basic modules
including necessary libraries, loading
and writing into the CSV file
"""
# Import necessary libraries
import pandas as pd

# Load the data into the dataframe
df = pd.read_csv('placements_data.tsv', sep='\t')

# Write the CSV file
df.to_csv('placements_data.csv', index=False)
