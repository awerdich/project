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
    file_path_list = [os.path.dirname(file) for file in file_list]
    file_name_list = [os.path.basename(file) for file in file_list]
    file_df = pd.DataFrame({'filename': file_name_list, 'path': file_path_list})
    return file_df

if __name__ == '__main__':
    file_df = create_file_list()
    print(file_df['path'].to_list())
    print(file_df['filename'].to_list())
    file_df.to_csv('file_list.csv', index=False)
