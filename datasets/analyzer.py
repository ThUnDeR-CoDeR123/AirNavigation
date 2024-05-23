import csv

# Read unique airport codes from the first CSV file
rows1 = set()
rows1_2=set()
with open("Full_Merge_of_All_Unique Airports.csv", 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields1 = next(csvreader)  # Skip header
    for row in csvreader:
        if row[1]:  # Ensure the value is not empty
            rows1.add(row[1])
            

# Read unique route codes from the second CSV file
rows2 = set()
rows2_2 = set()
with open("Full_Merge_of_All_Unique_Routes.csv", 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields2 = next(csvreader)  # Skip header
    for row in csvreader:
        if row[1]:  # Ensure the value is not empty
            rows2.add(row[1])
            rows2_2.add(row[2])

# Find the difference between the two sets
difference = rows2 - (rows1)

# Print the difference
print((difference), len(rows1-rows2),len(rows1),len(rows2),len(rows1-rows2_2))
# CGA (IATA)