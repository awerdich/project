#!/home/andreas/data/project_code/.venv/bin/python

import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    """ Returns True if there is enough space. False otherwise """
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100*du.free / du.total
    # Calculate how many free gigabytes
    # This is the version we want to keep.
    gigabytes_fee = du.free/2**30
    if percent_free < min_percent or gigabytes_fee < min_absolute:
        return False
    return True

if __name__ == "__main__":
    min_absolute = 2
    min_percent = 10
    print('Checking available disk space.')
    print(f'Minimum disk space: {min_absolute} GiB.')
    print(f'Minimum disk space: {min_percent} percent.')
    if not check_disk_usage(disk='/', min_absolute=min_absolute, min_percent=min_percent):
        print('WARNING: Not enough disk space.')
    else:
        print('Everything is ok.')
