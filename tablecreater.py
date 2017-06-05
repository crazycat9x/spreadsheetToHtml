import subprocess
from listToHtml import listToHtml
from excelToList import excelToList

def Main():
	style = open("style.css","r").read()
	target = "target.xlsx"
	final = "final.txt"
	tbl = excelToList(target)
	listToHtml(tbl,final)
	f = open(final)
	toClipBoard = f.read()
	f.close()
	toClipBoard = "<div><style scoped>" + style + "</style><div class = \"datagrid\">" + toClipBoard + "</div></div>"
	subprocess.run(['clip.exe'], input=toClipBoard.encode('utf-16'), check=True)
	
Main()

