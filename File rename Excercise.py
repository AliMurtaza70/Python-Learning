import os

folder_path = "icons"
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for i, filename in enumerate(files, start=1):
    new_name = f"icon{i}.png"
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)

