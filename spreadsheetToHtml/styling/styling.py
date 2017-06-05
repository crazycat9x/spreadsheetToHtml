def style(target, style):
    style = open(style,"r").read()
    temp = open(target).read()
    temp = "<div><style scoped>" + style + "</style><div class = \"datagrid\">" + temp + "</div></div>"
    final = open(target, "w", encoding="utf-8")
    final.write(temp)
