from pathlib import Path
from glob import glob
import re

def listdir(pathname, result):
	root = Path(pathname)
	dirs = []
	if(root.is_dir()):
		contents = glob("./"+str(root)+"/*")
		for inode in contents:
			inode = Path(inode)
			if(inode.is_dir()):
				result.append(str(inode))
				#dirs.append(inode)
			else:
				result.append(str(inode))
	else:
		print("Diretorio não encontrado ou sem permissão.")
		return None
	for directory in dirs:
		listdir(directory, result)
	return result

def search_regex_basic(line, matches, i):
	rgx = [
	"base64_decode\(\"[A-Za-z0-9]{32,}",
	"error_reporting\(0\)",
	"error_log\(0\)",
	'eval\/\*([\w]{1,6})\*\/\(\$?([A-Za-z]{1})[-A-Za-z0-9_]+',
	'\$[A-Za-z]([A-Za-z0-9]{1,9}\[\'[A-Za-z0-9]{3,6}\'\])\['
	]
	combinergx = "(" + ")|(".join(rgx) +")"
	match = re.search(combinergx, line)
	if match:
		#match = unicode(match.group(0)[:40], errors='replace')
		match = match.group(0)[:40]
		matches += [[match, i]]
	return matches

def search_file(arquivo, dic):
	matches = []
	numline = 1
	for line in arquivo:
		matches = search_regex_basic(line, matches, numline)
		if(matches):
			dic[arquivo.name] = matches
		numline+=1

def show_matches(dic):
	for arq, line in zip(dic.keys(), dic.values()):
		print("# {}: ".format(arq))
		for match in line:
			print("Match on line {}: {}".format(match[1], match[0]))

def main():
	print("Scanner simples em Python.")
	diretorio = input("Informe o diretório a escanear: ")
	allfiles = listdir(diretorio, [])
	for fl in allfiles:
		arquivo = open(fl, 'r', encoding='latin1')
		files_matches = {}
		search_file(arquivo, files_matches)
		show_matches(files_matches)
		arquivo.close()

	print("\n\nO scan procurou a partir dos padrões abaixo: ")
	rgx = [
	"base64_decode\(\"[A-Za-z0-9]{32,}",
	"error_reporting\(0\)",
	"error_log\(0\)",
	'eval\/\*([\w]{1,6})\*\/\(\$?([A-Za-z]{1})[-A-Za-z0-9_]+',
	'\$[A-Za-z]([A-Za-z0-9]{1,9}\[\'[A-Za-z0-9]{3,6}\'\])\['
	]
	for r in rgx:
		print(r)

if __name__ == '__main__':
	main()