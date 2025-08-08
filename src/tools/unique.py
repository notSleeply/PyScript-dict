import os

def get_unique_filename(filepath):
    if not os.path.exists(filepath):
        return filepath
    directory = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_filename = f"{name}{counter}{ext}"
        new_filepath = os.path.join(directory, new_filename)
        if not os.path.exists(new_filepath):
            return new_filepath
        counter += 1

def get_unique_dir(base_dir):
    if not os.path.exists(base_dir):
        return base_dir
    counter = 1
    while True:
        new_dir = f"{base_dir}_{counter}"
        if not os.path.exists(new_dir):
            return new_dir
        counter += 1