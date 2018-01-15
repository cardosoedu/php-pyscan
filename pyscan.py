import subprocess
import shlex
import os
from glob import glob

cmds = [
        "egrep --include='*.php' -lr 'eval\/\*'",
        "egrep --include='*.php' -lr '\!?define\('ALREADY_RUN_'",
        "egrep --include='*.php' -lr '\$[A-Za-z]{1,}=Array\(\$[a-z]{1}[0-9A-Za-z]{1,10}\['"
        ]

# input patterns file or leave blank (use 10 simple patterns)
# input directory to search or leave blank (search current directory)
# recursive search for php files
# search inside file

def searchFile(file, patterns):
	None

def RecursiveSearch(dirname, result):
	tmpDirs = []

	if(os.path.isdir(dirname)):
		contentsOfDir = glob(str(dirname)+'/*')
		for node in contentsOfDir:
			print(node)
			if(os.path.isdir(node)):
				tmpDirs.append(node)
			else:
				if('.php' in os.path.basename(node)):
					result.append(node)
	else:
		exit("%s is not a directory." % dirname)

	for directory in tmpDirs:
		try:
			RecursiveSearch(directory, result)
		except PermissionError:
			pass
	return result

#work in progress