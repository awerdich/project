#!/home/andreas/data/project_code/.venv/bin/python

import psutil

def check_memory():
    """Gets the current process's memory usage in Mbytes."""
    mib = 2**20
    process = psutil.Process()
    memory_info = process.memory_info()
    output = memory_info.rss/mib
    return output

def main():
    """ Prints that everything is OK if there is enough free memory """
    memory_usage = check_memory()
    if not check_memory() > 10:
        print(f'ERROR: Memory usage: {memory_usage} MB')
    else:
        print('Memory check: OK.')

if __name__ == '__main__':
    main()