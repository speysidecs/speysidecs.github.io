
import os

folder_path = r"C:\Users\mdcmc\Desktop\GitHub\speysidecs.github.io\sdd"
line_to_add = "[<- Return Home](https://speysidecs.github.io/)"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Open the file in read mode and read its content
        with open(file_path, 'r') as file:
            content = file.read()

        # Open the file in write mode and write the new line at the beginning
        with open(file_path, 'w') as file:
            file.write(line_to_add + '\n' + content)

print("Lines added to all files.")