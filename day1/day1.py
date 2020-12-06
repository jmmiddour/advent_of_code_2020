############### Report Repair ###############

# Find the two entries that sum to 2020; 
# What do you get if you multiply them together?

import pandas as pd

# Create a variable to hold data from list.txt
values = pd.read_csv('list.csv', header=None)

# Look at the values to verify loaded correctly
# print(values)

# Remove column 1
values.drop(columns = 1, inplace=True)

# Check that it worked
# print(values)

# Remove duplicates from values
values.drop_duplicates()

# Find the lowest value
# print(values[0].value_counts(sort=False, bins=8))

# Find the highest number I would be able to use
print(2020 - 323)  # returned 1697

# Remove values that are too high
new_vals = values[values[0] < 1697]

# Look at the shape of values now, was 200 rows
print('New Number of Rows: ', new_vals.shape[0])

# Look at the value counts binned to verify change
print(new_vals[0].value_counts(sort=False, bins=8))

############### Part 1 ###############
# Find 2 values that == 2020
# Then multiple those two values
for i in new_vals[0]:
    for j in new_vals[0]:
        if i + j == 2020:
            print(f'{i} + {j} = 2020')
            print(f'The product of {i} and {j} is {i * j}')

############### Part 2 ###############
# Find 3 values that == 2020
# Then multiple those two values
for i in values[0]:
    for j in values[0]:
        for k in values[0]:
            if i + j + k == 2020:
                print(f'{i} + {j} + {k} = 2020')
                print(f'The product of {i}, {j}, and {k} is {i * j * k}')
