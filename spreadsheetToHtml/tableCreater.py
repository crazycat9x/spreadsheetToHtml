# -*- coding: utf-8 -*-

import subprocess
import excelConverse
import styling
from tkinter.filedialog import askopenfilename, asksaveasfilename


def Main():
    target = askopenfilename(title="Choose spreadsheet file.")
    style = askopenfilename(filetypes=(("Cascading style sheet file", "*.css"), ("All Files", "*.*")),
                            title="Choose CSS file.")
    final = asksaveasfilename(defaultextension=".txt")
    tbl = excelConverse.excelToList(target)
    excelConverse.listToHtml(tbl, final)
    styling.style(final, style)
    toClipBoard = open(final, "r", encoding = "utf-8").read()
    subprocess.run(['clip.exe'], input=toClipBoard.encode("utf-8"), check=True)


Main()
