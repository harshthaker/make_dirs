import os

list_array = [1,2,3,4]

def create_dirs(path):
    for dir_name in unique_labels:
        output_path = os.path.join(path, dir_name)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
