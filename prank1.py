import os

def rename_files():
    file_list = os.listdir(r"E:\Udacity\Python\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"E:\Udacity\Python\prank")

    for file_name in file_list:
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(saved_path)
rename_files()
