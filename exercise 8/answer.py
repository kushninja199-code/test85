import os
folder = "exercise 8"
folders = os.listdir(folder)
print(folders)
a=1
for file in folders:
    file=str(file)
    if file[-4:]==".png":
        os.rename(f"{folder}/{file}",f"{folder}/{a}.png")
        a+=1
    else:
        continue

# or

# import os
# folder = "exercise 8"
# folders = os.listdir(folder)
# print(folders)
# for i, name in enumerate(folders):
#     if name.endswith(".png"):
#         old_path = os.path.join(folder, name)    # os.path.join is a Python function that combines path components into a single file path.
#         new_path = os.path.join(folder, f"{i+1}.png")
#         print(old_path)
#         os.rename(old_path, new_path)