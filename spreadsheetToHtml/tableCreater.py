import os
import subprocess
from excelConverse import *
from styling import *
from tkinter.filedialog import *

def Main():
	target = askopenfilename(title = "Choose spreadsheet file.")
	style = askopenfilename(filetypes =(("Cascading style sheet file", "*.css"),("All Files","*.*")),title = "Choose CSS file.")
	final = asksaveasfilename(defaultextension=".txt")
	tbl = excelToList(target)
	listToHtml(tbl,final)
	styling(final, style)
	toClipBoard = open(final,"r").read()
	subprocess.run(['clip.exe'], input=toClipBoard.encode('utf-8'), check=True)	
Main()

