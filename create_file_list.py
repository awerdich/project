#!/home/andreas/data/project_code/.venv/bin/python

import os
import glob
import pandas as pd

def create_file_list(extension='.py'):
    """
    Generates a DataFrame containing file names and their respective paths
    for files in the current working directory.
    """
    file_list = glob.glob(os.path.join(os.getcwd(), f'*{extension}'), recursive=False)
    return file_list

def convert_df(file_list):
    """ Converts a file list to a DataFrame """
    file_path_list = [os.path.dirname(file) for file in file_list]
    file_name_list = [os.path.basename(file) for file in file_list]
    file_df = pd.DataFrame({'filename': file_name_list, 'path': file_path_list})
    return file_df

if __name__ == '__main__':
    # Retrieve the files from the working directory
    file_list = create_file_list()
    # Create a data frame from the list
    file_df = convert_df(file_list)
    print(file_df['filename'].to_list())
    file_df.to_csv('file_list.csv', index=False)
