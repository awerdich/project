#!/home/andreas/data/project_code/.venv/bin/python

import shutil
import psutil

mib = 2**20
gib = 2**30

def check_disk_usage(disk, min_absolute, min_percent):
    """ Returns True if there is enough disk free space, false otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100*du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_fee = du.free/gib
    if percent_free < min_percent or gigabytes_fee < min_absolute:
        return False
    return True

def check_memory():
    """Gets the current process's memory usage in bytes."""
    process = psutil.Process()
    memory_info = process.memory_info()
    output = memory_info.rss/mib
    return output

if __name__ == "__main__":
    if not check_disk_usage(disk='/', min_absolute=2, min_percent=10):
        print('ERROR: Not enough disk space.')
    else:
        print('Disk space check: OK')
    memory_usage = check_memory()
    if not check_memory() > 10:
        print(f'ERROR: Memory usage: {memory_usage} MB')
    else:
        print('Memory check: OK.')


    
