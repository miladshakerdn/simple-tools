# Description:
# This script is used to rename files in script directory.
# Usage: python renameFileName.py <name_to_replace> <name_to_replace_with>

# Todo list for next version:
# 1. Add a function to get the directory path from user (ui or cli) []
# 2. Add a function to rename specific files in a directory []
# 3. crawling all files in a directory and subdirectories []
# 4. WTF, linux do it simply... f**k windows [x]

# Author: Milad Shaker
# Lindin: https://www.linkedin.com/in/milad-shaker-ba7ab6141/
# Github: https://github.com/miladshakerdn/simple-tools


import os
import sys
# get list of files in this directory
def get_files():
    files = os.listdir(os.getcwd())
    return files

# rename files in this directory and replace them with new names and return the new names
def rename_files(name_to_replace,name_to_replace_with = ""):
    files = get_files()
    for file in files:
        new_name = file.replace(name_to_replace, name_to_replace_with)
        os.rename(file, new_name)
    return get_files()

if __name__ == "__main__":
    # get input from user cli, without use input() function
    name_to_replace         = sys.argv[1]
    name_to_replace_with    = sys.argv[2]
    print(rename_files(name_to_replace,name_to_replace_with))