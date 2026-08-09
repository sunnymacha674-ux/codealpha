import os
import shutil
import re

source_folder = "MyFiles"

destination_folder = os.path.join(source_folder, "images")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):

    if re.search(r"\.jpg$", filename, re.IGNORECASE):

        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)

        print(filename, "moved successfully!")

print("Task completed.")