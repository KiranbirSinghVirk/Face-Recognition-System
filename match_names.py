import os

def save_names_to_file(file_path, names_list):
    try:
        with open(file_path, 'w') as file:
            for name in names_list:
                file.write(f"{name}\n")
        print(f"Names successfully saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving names: {e}")

def check_name_in_file(file_path, target_name):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            
            # Check if the target name is in any line
            if any(target_name in line for line in lines):
                print(f"The name '{target_name}' is found in the file.")
            else:
                print(f"The name '{target_name}' is not found in the file.")
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "Student_names/names_list.txt"  # Replace with the desired path and filename
loadName=input("enter name")
names_list = []  # Replace with your list of names
names_list.append(loadName)
# Save names to file
save_names_to_file(file_path, names_list)

# Check if a particular name is in the file
target_name = input("Enter the name to check: ")
check_name_in_file(file_path, target_name)
