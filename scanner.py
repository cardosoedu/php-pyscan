import os
from glob import glob

def RecursiveSearch(directory, array):
    # Temporary list of directories
    tmpDirs = []
    # If the given path is a directory, then we'll continue
    if os.path.isdir(directory):
        # Get the contents of said directory with glob
        contentsOfDir = glob(str(directory)+'/*')
        # For each node (file or dir) in the list we'll append to the array given to the function
        for node in contentsOfDir:
            array.append(node)
            # If the node is a directory, we'll add it to the temporary list of directories
            if(os.path.isdir(node)):
                tmpDirs.append(node)

        if(tmpDirs):
            # For each node inside the temp list
            for node in tmpDirs:
                try:
                    # Recursively search inside that directory
                    RecursiveSearch(node, array)
                except PermissionError:
                    # if there's a debug flag active, we'll print whenever we get a permission denied
                    if(dbg):
                        print("Warning: permission denied in {}!".format(node))
                    pass
        return array
    else:
        exit('Not a directory.')

if __name__ == '__main__':
    print('Temporary Name here')
    lista = RecursiveSearch('.', [])
    print(sorted(lista))
