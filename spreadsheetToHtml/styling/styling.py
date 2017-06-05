def style(target, cssFile):
    cssFile = open(cssFile, "r").read()
    temp = open(target).read()
    temp = "<div><style scoped>" + cssFile + "</style><div class = \"datagrid\">" + temp + "</div></div>"
    final = open(target, "w")
    final.write(temp)
