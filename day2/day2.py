############### Password Philosophy ###############

# Each line gives the password policy and then the password. 
# The password policy indicates the lowest and highest number of times 
#   a given letter must appear for the password to be valid. 
# For example, 1-3 a means that the password must contain "a" 
#   at least 1 time and at most 3 times.
# To try to debug the problem, they have created a list (your puzzle input) 
#   of passwords (according to the corrupted database) and the 
#   corporate policy when that password was set.

# How many passwords are valid according to their policies?

import pandas as pd

# Create a variable to hold data from list.txt
pws = pd.read_csv('passwords.csv')

# Look at the passwords to verify it loaded correctly
# print(pws)

# Split the columm pol_num into 2 columns for start and end
pws[['start', 'end']] = pws.pol_num.str.split('-', expand=True)

# Type values in start and end as an integers
pws['start'] = pd.to_numeric(pws['start'])
pws['end'] = pd.to_numeric(pws['end'])

# Look at the new passwords to verify it split correctly
# print(pws)

# Reorder the columns with only the columns I need now
pws = pws[['start', 'end', 'char', 'password']]

# Look at the new passwords to verify it is ordered correctly
# print(pws.dtypes)

# Iterate through the passwords to compare them to the policy
counter = 0
for i in pws['char']:
    for j in pws['password']:
        if j in i:
            num_ltr = i.count(j)
            for s in pws['start']:
                for e in pws['end']:
                    if num_ltr >= s and num_ltr <= e:
                        counter += 1

print(f'Number of valid passwords: {counter}')


# with open('input2.txt', 'r') as input_file: 
#     input_list = [[[int(n) for n in i.split(' ')[0].split('-')], 
#     i.split(' ')[1][0], 
#     i.split(' ')[2]] 
#     for i in input_file.read().split('\n')]; 
#     print(str([(pwd[2].count(pwd[1]) >= pwd[0][0]) and 
#     (pwd[2].count(pwd[1]) <= pwd[0][1]) for pwd in input_list]
#     .count(True)) + '\n' + str([(pwd[2][pwd[0][0] - 1] == pwd[1])
#      ^ (pwd[2][pwd[0][1] - 1] == pwd[1]) for pwd in input_list]
#      .count(True)))