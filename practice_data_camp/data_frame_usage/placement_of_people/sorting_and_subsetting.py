"""
To perform sorting and subseting
of dataframe, we do the following
"""
# Import necessary libraries
import pandas as pd

# Load the data into the dataframe
df = pd.read_csv('placements_data.tsv', sep='\t')

# Write the CSV file
df.to_csv('placements_data.csv', index=False)

# Sort according to ascending/increasing  salary
# print(df.sort_values('salary'))

# To Sort in descdending/decreasing order of salary
# print(df.sort_values('salary', ascending=False))

# To Sort by multiple variables
# print(df.sort_values(['salary', 'gender'], ascending = [True, False]))

# To subset columns(print a particular column)
# print(df['specialisation'])

# To subset multiple columns
# print(df[["gender", "specialisation"]])

# Or (Another method to subset multiple column)
# cols_to_subset = ["gender", "specialisation"]
# print(df[cols_to_subset])

# To subset rows
# print(df[df['salary'] > 50000])

# To subset based on text data
# print(df[df['salary'] == 0])

# To subset based on dates(Assuming a date value is present)
# print(df[df['date_of_payment'] < "2015-01-01"])

# To subset based on multiple conditions
# ssc_b_central = df['ssc_b'] == 'Central'
# ssc_p_73 = df['ssc_p'] == 73
# print(df[ssc_b_central & ssc_p_73])

# To subset using .isin()
# is_science_or_art = df['degree_p'].isin(['Science', 'Arts'])
# print(df[is_science_or_art])

