import os

# Path to the folder on the F drive
folder_path = "F:\detdes\Student_names"

# Ensure the folder exists, create it if not
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Get names from user input
input_names = input("Enter names (separated by commas): ").split(',')

# Path to the file where the names will be stored
file_path = os.path.join(folder_path, "names_list.txt")

# Write the names to the file
with open(file_path, 'w') as file:
    file.write('\n'.join(input_names))

print("Names have been stored in", file_path)
