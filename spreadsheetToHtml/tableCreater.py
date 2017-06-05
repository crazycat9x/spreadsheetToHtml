import os
import subprocess
from excelConverse import *
from styling import *

def Main():
	target = os.path.abspath("target.xlsx")
	final = os.path.abspath("final.txt")
	tbl = excelToList(target)
	listToHtml(tbl,final)
	styling(final)
	toClipBoard = open(final,"r").read()
	subprocess.run(['clip.exe'], input=toClipBoard.encode('utf-8'), check=True)	
Main()

