"""
Advent of Code 2022 Day 07
https://adventofcode.com/2022/day/7
AUTHOR: Alex Nazareth
DATE:   November 2023
Short description:
- Given input of filesystem navigation.
- Part 1: Find sum of all directories with filesize < 100,000.
- Part 2: Find smallest directory that when deleted will free up at least 30,000,000 units.
-- ie Size of deleted directory + size of free space (out of 70,000,000 total) >= 30,000,000. 
"""

from collections import defaultdict

def main(data, isPart1 = True):
    dirs = defaultdict(int)
    cwd = '/'  # starting with outermost directory
    data.readline()  # omit first line containing '$ cd /'
    for r in data:
        parts = r[:-1].split(' ')  # omit newline character
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '..':
                    cwd = '/'.join(cwd.split('/')[:-2]) + '/'
                else:
                    cwd = cwd + parts[2] + '/'
            elif parts[1] == 'ls':
                pass
        elif parts[0] == 'dir':  # row contains directory info, no action necessary
            pass
        else:  # row contains file info (size)
            filesize = parts[0]
            for i in range(1, cwd.count('/') + 1):
                # add filesize to all ancestral directories
                dirname = '/'.join(cwd.split('/')[:-i]) + '/'
                dirs[dirname] += int(filesize)
    sum_small_dirs = sum([d for d in dirs.values() if d<100000])
    if isPart1:
        return sum_small_dirs 
    else:
        TOTAL_FS_SIZE = 70000000
        UPDATE_SPACE_REQ = 30000000
        free_space = TOTAL_FS_SIZE - dirs['/']
        min_filesize_req = UPDATE_SPACE_REQ - free_space
        return min([d for d in dirs.values() if d>=min_filesize_req])

if __name__ == '__main__':
    infile = 'input.txt'
    indata = open(infile, 'r')
    print(f"Part 1: The sum of all directories less than size 100,000 is: {str(main(indata))} units")
    indata.close()
    indata = open(infile, 'r')
    print("Part 2: To yield 30,000,000 units of free space, " +
          "the smallest directory that can be deleted is of size: " + str(main(indata, False)))
    indata.close()
    
